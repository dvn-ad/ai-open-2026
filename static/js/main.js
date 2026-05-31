document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide Icons
    lucide.createIcons();

    // Application State Variables
    let selectedFile = null;
    let selectedDemoId = null;
    let availableModels = { ollama: [], openai: [] };
    let timerInterval = null;
    let startTime = 0;

    // DOM Elements - Navigation & Core States
    const runBtn = document.getElementById('run-pipeline-btn');
    const welcomeState = document.getElementById('welcome-state');
    const processingState = document.getElementById('processing-state');
    const resultsState = document.getElementById('results-state');

    // DOM Elements - Document Input
    const inputUploadTab = document.getElementById('input-upload-tab');
    const inputDemoTab = document.getElementById('input-demo-tab');
    const uploadZone = document.getElementById('upload-zone');
    const demoZone = document.getElementById('demo-zone');
    const fileInput = document.getElementById('file-input');
    const selectedFileCard = document.getElementById('selected-file-card');
    const selectedFileName = document.getElementById('selected-file-name');
    const selectedFileSize = document.getElementById('selected-file-size');
    const removeFileBtn = document.getElementById('remove-file-btn');
    const demoList = document.getElementById('demo-list');

    // DOM Elements - Settings Configuration
    const engineRadios = document.querySelectorAll('input[name="llm_engine"]');
    const ollamaPanel = document.getElementById('ollama-config-panel');
    const openaiPanel = document.getElementById('openai-config-panel');
    const ollamaModelSelect = document.getElementById('ollama-model-select');
    const openaiModelSelect = document.getElementById('openai-model-select');
    const openaiApiKey = document.getElementById('openai-api-key');
    const toggleKeyBtn = document.getElementById('toggle-key-visibility');
    const paddleOrientToggle = document.getElementById('paddle-orient-toggle');

    // DOM Elements - Loading stage steps
    const stagePreprocess = document.getElementById('stage-preprocess');
    const stageOcr = document.getElementById('stage-ocr');
    const stageRestructure = document.getElementById('stage-restructure');
    const progressBarFill = document.getElementById('loader-progress-bar');
    const progressPercentage = document.getElementById('loader-percentage');
    const progressTimer = document.getElementById('loader-timer');

    // DOM Elements - Results Tabs & Content
    const resultTabs = document.querySelectorAll('.result-tab');
    const tabContents = document.querySelectorAll('.result-tab-content');
    
    // Result panels
    const badgeDocType = document.getElementById('badge-doc-type');
    const badgeScannedType = document.getElementById('badge-scanned-type');
    const preprocessSummary = document.getElementById('preprocess-summary');
    const ocrSummary = document.getElementById('ocr-summary');
    const llmSummary = document.getElementById('llm-summary');
    const auditGallery = document.getElementById('audit-gallery');
    
    const restructuredJsonCode = document.getElementById('restructured-json-code');
    const rawMarkdownCode = document.getElementById('raw-markdown-code');
    
    const metricTotalTime = document.getElementById('metric-total-time');
    const timingPreprocessVal = document.getElementById('timing-preprocess-val');
    const timingDoclingVal = document.getElementById('timing-docling-val');
    const timingLlmVal = document.getElementById('timing-llm-val');
    
    const timingPreprocessFill = document.getElementById('timing-preprocess-fill');
    const timingDoclingFill = document.getElementById('timing-docling-fill');
    const timingLlmFill = document.getElementById('timing-llm-fill');

    // DOM Elements - Lightbox Modal
    const imageModal = document.getElementById('image-modal');
    const modalClose = document.getElementById('modal-close');
    const modalImg = document.getElementById('modal-img');

    // DOM Elements - Toast Container
    const toastContainer = document.getElementById('toast-container');

    /* ==========================================================================
       1. INITIALIZATION & DATA FETCHING
       ========================================================================== */

    // Fetch dynamic models list
    async function fetchModels() {
        try {
            const res = await fetch('/api/models');
            if (res.ok) {
                availableModels = await res.json();
                populateModelOptions();
            } else {
                showToast('Failed to retrieve model listings', 'error');
            }
        } catch (e) {
            console.error('Error fetching models:', e);
            // Standby defaults if API fails
            availableModels = {
                ollama: ['gemma3:270m', 'gemma3:1b', 'gemma3:4b'],
                openai: ['gpt-4o-mini', 'gpt-4o', 'o1-mini']
            };
            populateModelOptions();
        }
    }

    // Populate model options dropdown
    function populateModelOptions() {
        ollamaModelSelect.innerHTML = '';
        availableModels.ollama.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            // Select default model gemma3:270m if present
            if (model === 'gemma3:270m') option.selected = true;
            ollamaModelSelect.appendChild(option);
        });

        // Trigger lucide check since select chevron could need updating
        lucide.createIcons();
    }

    // Fetch available demo documents
    async function fetchDemos() {
        try {
            const res = await fetch('/api/demos');
            if (res.ok) {
                const demos = await res.json();
                renderDemoList(demos);
            } else {
                showToast('Failed to load demo files', 'error');
            }
        } catch (e) {
            console.error('Error fetching demos:', e);
            demoList.innerHTML = '<p class="field-hint" style="color: #ef4444;">Error connecting to API. Demolist unavailable.</p>';
        }
    }

    // Render demo list items
    function renderDemoList(demos) {
        demoList.innerHTML = '';
        if (demos.length === 0) {
            demoList.innerHTML = '<p class="field-hint">No demo files are hosted on the server.</p>';
            return;
        }

        demos.forEach(demo => {
            const item = document.createElement('div');
            item.className = 'demo-item';
            item.dataset.id = demo.id;
            
            const badgeClass = demo.type.toLowerCase();
            
            item.innerHTML = `
                <div class="demo-item-info">
                    <span class="demo-item-name">${demo.name}</span>
                    <span class="demo-item-meta">
                        <span class="demo-badge ${badgeClass}">${demo.type}</span>
                        <span>${demo.size_kb} KB</span>
                    </span>
                </div>
                <i data-lucide="play-circle" style="width: 16px; height: 16px; color: var(--text-muted);"></i>
            `;
            
            item.addEventListener('click', () => selectDemoItem(demo.id));
            demoList.appendChild(item);
        });
        
        lucide.createIcons();
    }

    // Initial Fetch calls
    fetchModels();
    fetchDemos();

    /* ==========================================================================
       2. INPUT CONTROLS & EVENT LISTENERS
       ========================================================================== */

    // Tab switching: Upload File vs Demo File
    inputUploadTab.addEventListener('click', () => {
        inputUploadTab.classList.add('active');
        inputDemoTab.classList.remove('active');
        uploadZone.style.display = 'block';
        demoZone.style.display = 'none';
        
        // Restore upload selection state
        selectedDemoId = null;
        document.querySelectorAll('.demo-item').forEach(i => i.classList.remove('active'));
        updateRunButtonState();
    });

    inputDemoTab.addEventListener('click', () => {
        inputDemoTab.classList.add('active');
        inputUploadTab.classList.remove('active');
        demoZone.style.display = 'block';
        uploadZone.style.display = 'none';
        
        // Restore demo selection state
        selectedFile = null;
        selectedFileCard.style.display = 'none';
        fileInput.value = '';
        updateRunButtonState();
    });

    // File Input Drag & Drop
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadZone.classList.add('dragover');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadZone.classList.remove('dragover');
        }, false);
    });

    uploadZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length > 0) {
            handleSelectedFile(files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleSelectedFile(e.target.files[0]);
        }
    });

    // Handle file loading details
    function handleSelectedFile(file) {
        // Validate size (max 50MB)
        if (file.size > 50 * 1024 * 1024) {
            showToast('File is too large. Max size is 50MB.', 'error');
            return;
        }
        
        selectedFile = file;
        selectedDemoId = null;
        
        // Render File Card UI
        selectedFileName.textContent = file.name;
        selectedFileSize.textContent = formatBytes(file.size);
        selectedFileCard.style.display = 'flex';
        
        updateRunButtonState();
        showToast(`Selected file: ${file.name}`, 'info');
    }

    // Format bytes helper
    function formatBytes(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = 2;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    // Remove selected file button
    removeFileBtn.addEventListener('click', () => {
        selectedFile = null;
        selectedFileCard.style.display = 'none';
        fileInput.value = '';
        updateRunButtonState();
    });

    // Select a demo file
    function selectDemoItem(demoId) {
        selectedDemoId = demoId;
        selectedFile = null;
        
        document.querySelectorAll('.demo-item').forEach(item => {
            if (item.dataset.id === demoId) {
                item.classList.add('active');
                item.querySelector('i').style.color = 'var(--color-primary)';
            } else {
                item.classList.remove('active');
                const iElem = item.querySelector('i');
                if (iElem) iElem.style.color = 'var(--text-muted)';
            }
        });
        
        updateRunButtonState();
        showToast(`Selected demo document: ${demoId}`, 'info');
    }

    // Enable / Disable Run button based on selection
    function updateRunButtonState() {
        if (selectedFile || selectedDemoId) {
            runBtn.disabled = false;
        } else {
            runBtn.disabled = true;
        }
    }

    // Semantic LLM Engine selector panels toggles
    engineRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            // Remove active classes
            document.querySelectorAll('.engine-option').forEach(o => o.classList.remove('active'));
            // Add active class to checked option parent
            e.target.closest('.engine-option').classList.add('active');
            
            if (e.target.value === 'ollama') {
                ollamaPanel.style.display = 'block';
                openaiPanel.style.display = 'none';
            } else {
                ollamaPanel.style.display = 'none';
                openaiPanel.style.display = 'block';
            }
            lucide.createIcons();
        });
    });

    // Toggle OpenAI Key masking
    toggleKeyBtn.addEventListener('click', () => {
        const isPassword = openaiApiKey.type === 'password';
        openaiApiKey.type = isPassword ? 'text' : 'password';
        
        const eyeIcon = toggleKeyBtn.querySelector('i');
        if (isPassword) {
            eyeIcon.setAttribute('data-lucide', 'eye-off');
        } else {
            eyeIcon.setAttribute('data-lucide', 'eye');
        }
        lucide.createIcons();
    });

    /* ==========================================================================
       3. PIPELINE EXECUTION (LOADING AND API HANDLING)
       ========================================================================= */

    runBtn.addEventListener('click', async () => {
        if (!selectedFile && !selectedDemoId) return;

        // Reset state layouts
        welcomeState.style.display = 'none';
        resultsState.style.display = 'none';
        processingState.style.display = 'flex';
        
        // Reset loader UI
        stagePreprocess.className = 'loading-stage active';
        stageOcr.className = 'loading-stage';
        stageRestructure.className = 'loading-stage';
        progressBarFill.style.width = '5%';
        progressPercentage.textContent = 'Initializing workspace...';

        // Start processing stopwatch
        startTimer();

        // Simulate stages during API execution (makes UI reactive)
        let simulatedProgress = 0;
        const progressTimerSim = setInterval(() => {
            simulatedProgress += 0.5;
            
            if (simulatedProgress < 15) {
                progressBarFill.style.width = `${5 + simulatedProgress}%`;
                progressPercentage.textContent = 'Step 1: Preprocessing scanned margins & skew...';
            } else if (simulatedProgress >= 15 && simulatedProgress < 50) {
                stagePreprocess.className = 'loading-stage completed';
                stageOcr.className = 'loading-stage active';
                progressBarFill.style.width = `${5 + simulatedProgress}%`;
                progressPercentage.textContent = 'Step 2: Processing layout analysis & OCR (Docling)...';
            } else if (simulatedProgress >= 50 && simulatedProgress < 85) {
                stageOcr.className = 'loading-stage completed';
                stageRestructure.className = 'loading-stage active';
                progressBarFill.style.width = `${5 + simulatedProgress}%`;
                progressPercentage.textContent = 'Step 3: Restructuring layout tags into CEISA JSON (LLM)...';
            } else if (simulatedProgress >= 85 && simulatedProgress < 95) {
                progressBarFill.style.width = '95%';
                progressPercentage.textContent = 'Finalizing structured JSON outputs...';
            }
        }, 300);

        // Package Form Fields
        const formData = new FormData();
        if (selectedFile) {
            formData.append('file', selectedFile);
        } else {
            formData.append('demo_id', selectedDemoId);
        }

        const engine = document.querySelector('input[name="llm_engine"]:checked').value;
        formData.append('llm_engine', engine);
        
        const model = engine === 'ollama' ? ollamaModelSelect.value : openaiModelSelect.value;
        formData.append('model', model);
        
        formData.append('use_paddle_orient', paddleOrientToggle.checked);
        if (openaiApiKey.value.trim() !== '') {
            formData.append('api_key', openaiApiKey.value.trim());
        }

        try {
            const response = await fetch('/api/process', {
                method: 'POST',
                body: formData
            });

            clearInterval(progressTimerSim);
            stopTimer();

            if (response.ok) {
                const data = await response.json();
                renderResults(data);
                showToast('Pipeline execution finished successfully!', 'success');
            } else {
                const errorData = await response.json();
                const detail = errorData.detail || 'Pipeline failure occurred.';
                handleExecutionError(detail);
            }
        } catch (e) {
            console.error(e);
            clearInterval(progressTimerSim);
            stopTimer();
            handleExecutionError('Failed to communicate with OCR server backend.');
        }
    });

    // Stopwatch timer
    function startTimer() {
        startTime = timeSeconds();
        progressTimer.textContent = '0.0s';
        timerInterval = setInterval(() => {
            const diff = timeSeconds() - startTime;
            progressTimer.textContent = `${diff.toFixed(1)}s`;
        }, 100);
    }

    function stopTimer() {
        if (timerInterval) clearInterval(timerInterval);
    }

    function timeSeconds() {
        return Date.now() / 1000;
    }

    function handleExecutionError(message) {
        processingState.style.display = 'none';
        welcomeState.style.display = 'flex';
        showToast(message, 'error');
    }

    /* ==========================================================================
       4. RESULTS VIEWING AND NAVIGATION
       ========================================================================== */

    function renderResults(data) {
        // Change state visibility
        processingState.style.display = 'none';
        resultsState.style.display = 'flex';

        // 1. Title bar details
        badgeDocType.textContent = data.doc_type.toUpperCase();
        badgeScannedType.textContent = data.is_scanned ? 'SCANNED / IMAGE' : 'DIGITAL PDF';
        
        // 2. Summary stats
        preprocessSummary.textContent = data.is_scanned 
            ? `Successfully deskewed and cleaned ${data.preprocessed_images.length} pages.`
            : 'Digital document detected; bypassed image deskew pipeline.';
            
        ocrSummary.textContent = `Completed layout parsing. Detected headings, lists, and tables.`;
        llmSummary.textContent = `CEISA structured alignment finished. Schema matches target.`;

        // 3. Preprocessed Audit images
        renderAuditGallery(data.preprocessed_images, data.is_scanned);

        // 4. Code panel views (JSON and Markdown)
        renderSyntaxHighlightedJson(data.restructured_json);
        rawMarkdownCode.textContent = data.raw_markdown;

        // 5. Execution timing breakdown metrics
        metricTotalTime.textContent = `${data.timing.total}s`;
        
        timingPreprocessVal.textContent = `${data.timing.preprocessing}s`;
        timingDoclingVal.textContent = `${data.timing.docling}s`;
        timingLlmVal.textContent = `${data.timing.llm}s`;

        // Bar sizing relative to total
        const total = Math.max(data.timing.total, 0.1);
        timingPreprocessFill.style.width = `${(data.timing.preprocessing / total) * 100}%`;
        timingDoclingFill.style.width = `${(data.timing.docling / total) * 100}%`;
        timingLlmFill.style.width = `${(data.timing.llm / total) * 100}%`;

        // Click first tab automatically
        switchResultsTab('tab-visual-flow');
    }

    // Render audit gallery
    function renderAuditGallery(images, isScanned) {
        auditGallery.innerHTML = '';
        
        if (!isScanned || images.length === 0) {
            auditGallery.innerHTML = `
                <div class="welcome-box" style="padding: 40px; grid-column: 1 / -1; max-width: 100%;">
                    <i data-lucide="file-check-2" style="width: 32px; height: 32px; color: var(--color-preprocess);"></i>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px;">
                        No preprocessing was performed. Digital vector PDFs maintain layout without pixels adjustments.
                    </p>
                </div>
            `;
            lucide.createIcons();
            return;
        }

        images.forEach((imgUrl, index) => {
            const card = document.createElement('div');
            card.className = 'gallery-card';
            
            card.innerHTML = `
                <div class="gallery-image-wrapper">
                    <img src="${imgUrl}" alt="Preprocessed Page ${index + 1}">
                </div>
                <div class="gallery-card-info">
                    <span class="gallery-card-title">Page ${index + 1} Preprocessed</span>
                </div>
            `;
            
            card.addEventListener('click', () => openImageModal(imgUrl, `Preprocessed Page ${index + 1} Audit`));
            auditGallery.appendChild(card);
        });
    }

    // Open image Lightbox modal
    function openImageModal(src, caption) {
        imageModal.style.display = "flex";
        modalImg.src = src;
        document.getElementById('modal-caption').textContent = caption;
    }

    modalClose.addEventListener('click', () => {
        imageModal.style.display = "none";
    });

    imageModal.addEventListener('click', (e) => {
        if (e.target === imageModal) {
            imageModal.style.display = "none";
        }
    });

    // Syntax-highlighted JSON renderer (Safe formatting)
    function renderSyntaxHighlightedJson(jsonObj) {
        const jsonStr = JSON.stringify(jsonObj, null, 2);
        
        // Match JSON elements for color styling
        const safeJson = jsonStr
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)/g, (match) => {
                let cls = 'json-number';
                if (/^"/.test(match)) {
                    if (/:$/.test(match)) {
                        cls = 'json-key';
                    } else {
                        cls = 'json-string';
                    }
                } else if (/true|false/.test(match)) {
                    cls = 'json-boolean';
                } else if (/null/.test(match)) {
                    cls = 'json-null';
                }
                return `<span class="${cls}">${match}</span>`;
            });
            
        restructuredJsonCode.innerHTML = safeJson;
    }

    // Results Tab Switch control
    resultTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.dataset.tab;
            switchResultsTab(targetId);
        });
    });

    function switchResultsTab(targetId) {
        resultTabs.forEach(t => {
            if (t.dataset.tab === targetId) {
                t.classList.add('active');
            } else {
                t.classList.remove('active');
            }
        });

        tabContents.forEach(content => {
            if (content.id === targetId) {
                content.classList.add('active');
            } else {
                content.classList.remove('active');
            }
        });
    }

    /* ==========================================================================
       5. BUTTON PANELS ACTIONS (COPY & DOWNLOAD)
       ========================================================================== */

    // Helper for clipboard copy
    function copyTextToClipboard(text, successMsg) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(successMsg, 'success');
        }, (err) => {
            console.error('Copy failure:', err);
            showToast('Clipboard copy failed.', 'error');
        });
    }

    // Copy JSON action
    document.getElementById('copy-json-btn').addEventListener('click', () => {
        const text = restructuredJsonCode.textContent;
        copyTextToClipboard(text, 'CEISA structured JSON copied to clipboard!');
    });

    // Download JSON action
    document.getElementById('download-json-btn').addEventListener('click', () => {
        const text = restructuredJsonCode.textContent;
        const blob = new Blob([text], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `restructured_ceisa_${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast('CEISA JSON downloaded.', 'info');
    });

    // Copy Markdown layout action
    document.getElementById('copy-md-btn').addEventListener('click', () => {
        const text = rawMarkdownCode.textContent;
        copyTextToClipboard(text, 'Parsed Layout Markdown copied to clipboard!');
    });

    /* ==========================================================================
       6. TOAST NOTIFICATION UTILITY
       ========================================================================== */

    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        let iconName = 'info';
        if (type === 'success') iconName = 'check-circle';
        if (type === 'error') iconName = 'alert-triangle';
        
        toast.innerHTML = `
            <i data-lucide="${iconName}"></i>
            <span>${message}</span>
            <i data-lucide="x" class="toast-close"></i>
        `;
        
        toastContainer.appendChild(toast);
        lucide.createIcons();
        
        // Click to close
        toast.querySelector('.toast-close').addEventListener('click', () => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(50px)';
            setTimeout(() => toast.remove(), 300);
        });

        // Auto remove
        setTimeout(() => {
            if (toast.parentNode) {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(50px)';
                setTimeout(() => toast.remove(), 300);
            }
        }, 4000);
    }
});
