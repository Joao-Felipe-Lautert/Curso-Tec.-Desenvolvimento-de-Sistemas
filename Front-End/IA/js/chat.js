// JavaScript para funcionalidade do chat com API Groq

class ChatApp {
    constructor() {
        this.apiKey = localStorage.getItem('groq_api_key') || '';
        this.model = localStorage.getItem('groq_model') || 'llama-3.3-70b-versatile';
        this.temperature = parseFloat(localStorage.getItem('groq_temperature')) || 0.7;
        this.messages = [];
        this.isTyping = false;
        
        this.initElements();
        this.initEventListeners();
        this.loadSettings();
        this.checkApiKey();
    }
    
    initElements() {
        this.chatMessages = document.getElementById('chatMessages');
        this.chatInput = document.getElementById('chatInput');
        this.sendButton = document.getElementById('sendButton');
        this.clearButton = document.getElementById('clearChat');
        this.settingsButton = document.getElementById('settingsBtn');
        this.settingsModal = document.getElementById('settingsModal');
        this.closeSettingsButton = document.getElementById('closeSettings');
        this.saveSettingsButton = document.getElementById('saveSettings');
        this.cancelSettingsButton = document.getElementById('cancelSettings');
        this.apiKeyInput = document.getElementById('apiKey');
        this.modelSelect = document.getElementById('modelSelect');
        this.temperatureSlider = document.getElementById('temperature');
        this.temperatureValue = document.getElementById('temperatureValue');
        this.charCount = document.getElementById('charCount');
        this.status = document.getElementById('status');
        this.loadingOverlay = document.getElementById('loadingOverlay');
    }
    
    initEventListeners() {
        // Chat input events
        this.chatInput.addEventListener('input', () => this.handleInputChange());
        this.chatInput.addEventListener('keydown', (e) => this.handleKeyDown(e));
        
        // Send button
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Clear chat
        this.clearButton.addEventListener('click', () => this.clearChat());
        
        // Settings modal
        this.settingsButton.addEventListener('click', () => this.openSettings());
        this.closeSettingsButton.addEventListener('click', () => this.closeSettings());
        this.cancelSettingsButton.addEventListener('click', () => this.closeSettings());
        this.saveSettingsButton.addEventListener('click', () => this.saveSettings());
        
        // Settings inputs
        this.temperatureSlider.addEventListener('input', (e) => {
            this.temperatureValue.textContent = e.target.value;
        });
        
        // Suggestion buttons
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('suggestion-btn')) {
                const text = e.target.getAttribute('data-text');
                this.chatInput.value = text;
                this.handleInputChange();
                this.chatInput.focus();
            }
        });
        
        // Modal backdrop click
        this.settingsModal.addEventListener('click', (e) => {
            if (e.target === this.settingsModal) {
                this.closeSettings();
            }
        });
        
        // Auto-resize textarea
        this.chatInput.addEventListener('input', () => this.autoResizeTextarea());
    }
    
    handleInputChange() {
        const text = this.chatInput.value.trim();
        const charCount = this.chatInput.value.length;
        
        this.charCount.textContent = charCount;
        this.sendButton.disabled = !text || this.isTyping;
        
        // Hide suggestions when user starts typing
        const suggestions = document.querySelector('.suggestions');
        if (suggestions && text) {
            suggestions.style.display = 'none';
        } else if (suggestions && !text) {
            suggestions.style.display = 'block';
        }
    }
    
    handleKeyDown(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            if (!this.sendButton.disabled) {
                this.sendMessage();
            }
        }
    }
    
    autoResizeTextarea() {
        this.chatInput.style.height = 'auto';
        this.chatInput.style.height = Math.min(this.chatInput.scrollHeight, 120) + 'px';
    }
    
    async sendMessage() {
        const text = this.chatInput.value.trim();
        if (!text || this.isTyping) return;
        
        if (!this.apiKey) {
            this.showError('Por favor, configure sua chave da API Groq nas configurações.');
            this.openSettings();
            return;
        }
        
        // Add user message
        this.addMessage('user', text);
        this.chatInput.value = '';
        this.handleInputChange();
        this.autoResizeTextarea();
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            const response = await this.callGroqAPI(text);
            this.hideTypingIndicator();
            this.addMessage('ai', response);
        } catch (error) {
            this.hideTypingIndicator();
            this.showError('Erro ao comunicar com a API: ' + error.message);
        }
    }
    
    async callGroqAPI(message) {
        this.messages.push({ role: 'user', content: message });
        
        const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.apiKey}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: this.model,
                messages: this.messages,
                temperature: this.temperature,
                max_tokens: 2048,
                stream: false
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error?.message || `HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        const aiResponse = data.choices[0]?.message?.content || 'Desculpe, não consegui gerar uma resposta.';
        
        this.messages.push({ role: 'assistant', content: aiResponse });
        
        return aiResponse;
    }
    
    addMessage(type, text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        
        if (type === 'user') {
            avatar.textContent = 'U';
        } else {
            avatar.innerHTML = `
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="currentColor"/>
                </svg>
            `;
        }
        
        const bubble = document.createElement('div');
        bubble.className = 'message-bubble';
        
        const messageText = document.createElement('div');
        messageText.className = 'message-text';
        messageText.innerHTML = this.formatMessage(text);
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = Utils.formatTime(new Date());
        
        bubble.appendChild(messageText);
        bubble.appendChild(messageTime);
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(bubble);
        
        // Remove suggestions if they exist
        const suggestions = document.querySelector('.suggestions');
        if (suggestions) {
            suggestions.remove();
        }
        
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    formatMessage(text) {
        // Simple markdown-like formatting
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/`(.*?)`/g, '<code>$1</code>')
            .replace(/\n/g, '<br>');
    }
    
    showTypingIndicator() {
        this.isTyping = true;
        this.sendButton.disabled = true;
        this.status.textContent = 'IA está digitando...';
        
        const typingDiv = document.createElement('div');
        typingDiv.className = 'typing-indicator';
        typingDiv.id = 'typingIndicator';
        
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="currentColor"/>
                </svg>
            </div>
            <div class="typing-bubble">
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;
        
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.isTyping = false;
        this.sendButton.disabled = !this.chatInput.value.trim();
        this.status.textContent = 'Powered by Groq';
        
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
    
    clearChat() {
        const confirmClear = confirm('Tem certeza que deseja limpar toda a conversa?');
        if (confirmClear) {
            this.messages = [];
            
            // Keep only welcome message and suggestions
            const welcomeMessage = this.chatMessages.querySelector('.welcome-message');
            const suggestions = this.chatMessages.querySelector('.suggestions');
            
            this.chatMessages.innerHTML = '';
            
            if (welcomeMessage) {
                this.chatMessages.appendChild(welcomeMessage.cloneNode(true));
            }
            
            if (suggestions) {
                this.chatMessages.appendChild(suggestions.cloneNode(true));
            }
            
            Utils.showNotification('Conversa limpa com sucesso!', 'success');
        }
    }
    
    openSettings() {
        this.settingsModal.classList.add('active');
        this.apiKeyInput.focus();
    }
    
    closeSettings() {
        this.settingsModal.classList.remove('active');
    }
    
    loadSettings() {
        this.apiKeyInput.value = this.apiKey;
        this.modelSelect.value = this.model;
        this.temperatureSlider.value = this.temperature;
        this.temperatureValue.textContent = this.temperature;
    }
    
    saveSettings() {
        const newApiKey = this.apiKeyInput.value.trim();
        const newModel = this.modelSelect.value;
        const newTemperature = parseFloat(this.temperatureSlider.value);
        
        if (!newApiKey) {
            this.showError('Por favor, insira uma chave da API válida.');
            return;
        }
        
        this.apiKey = newApiKey;
        this.model = newModel;
        this.temperature = newTemperature;
        
        // Save to localStorage
        localStorage.setItem('groq_api_key', this.apiKey);
        localStorage.setItem('groq_model', this.model);
        localStorage.setItem('groq_temperature', this.temperature.toString());
        
        this.closeSettings();
        Utils.showNotification('Configurações salvas com sucesso!', 'success');
        this.checkApiKey();
    }
    
    checkApiKey() {
        if (!this.apiKey) {
            this.status.textContent = 'Configure sua API key';
            this.status.style.color = '#ef4444';
        } else {
            this.status.textContent = 'Powered by Groq';
            this.status.style.color = '';
        }
    }
    
    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.innerHTML = `
            <strong>Erro:</strong>
            ${message}
        `;
        
        // Remove existing error messages
        const existingErrors = this.chatMessages.querySelectorAll('.error-message');
        existingErrors.forEach(error => error.remove());
        
        this.chatMessages.appendChild(errorDiv);
        this.scrollToBottom();
        
        // Auto remove after 10 seconds
        setTimeout(() => {
            if (errorDiv.parentNode) {
                errorDiv.remove();
            }
        }, 10000);
    }
    
    showLoading() {
        this.loadingOverlay.classList.add('active');
    }
    
    hideLoading() {
        this.loadingOverlay.classList.remove('active');
    }
}

// Initialize chat app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Only initialize on chat page
    if (document.getElementById('chatMessages')) {
        window.chatApp = new ChatApp();
    }
});

// Add some helpful functions to window for debugging
window.ChatDebug = {
    clearStorage: function() {
        localStorage.removeItem('groq_api_key');
        localStorage.removeItem('groq_model');
        localStorage.removeItem('groq_temperature');
        console.log('Chat storage cleared');
    },
    
    getMessages: function() {
        return window.chatApp ? window.chatApp.messages : [];
    },
    
    testApiKey: async function(apiKey) {
        try {
            const response = await fetch('https://api.groq.com/openai/v1/models', {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                }
            });
            
            if (response.ok) {
                const data = await response.json();
                console.log('API Key válida! Modelos disponíveis:', data.data.map(m => m.id));
                return true;
            } else {
                console.error('API Key inválida:', response.statusText);
                return false;
            }
        } catch (error) {
            console.error('Erro ao testar API Key:', error);
            return false;
        }
    }
};
