// JavaScript para funcionalidades da página de contato

document.addEventListener('DOMContentLoaded', function() {
    initContactForm();
    initFAQ();
    initCharacterCounter();
});

// Inicializar formulário de contato
function initContactForm() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = submitBtn.querySelector('.btn-text');
    const btnLoading = submitBtn.querySelector('.btn-loading');
    
    if (!form) return;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Validar formulário
        if (!validateForm()) {
            return;
        }
        
        // Mostrar loading
        submitBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoading.style.display = 'flex';
        
        try {
            // Simular envio (em produção, enviar para servidor)
            await simulateFormSubmission();
            
            // Mostrar mensagem de sucesso
            showSuccessMessage();
            
            // Limpar formulário
            form.reset();
            updateCharacterCounter();
            
        } catch (error) {
            Utils.showNotification('Erro ao enviar mensagem. Tente novamente.', 'error');
        } finally {
            // Restaurar botão
            submitBtn.disabled = false;
            btnText.style.display = 'inline';
            btnLoading.style.display = 'none';
        }
    });
    
    // Validação em tempo real
    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => clearFieldError(input));
    });
}

// Validar formulário
function validateForm() {
    const form = document.getElementById('contactForm');
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!validateField(field)) {
            isValid = false;
        }
    });
    
    return isValid;
}

// Validar campo individual
function validateField(field) {
    const formGroup = field.closest('.form-group');
    const fieldName = field.getAttribute('name');
    let isValid = true;
    let errorMessage = '';
    
    // Limpar erros anteriores
    clearFieldError(field);
    
    // Validar campo obrigatório
    if (field.hasAttribute('required') && !field.value.trim()) {
        isValid = false;
        errorMessage = 'Este campo é obrigatório.';
    }
    
    // Validações específicas
    switch (fieldName) {
        case 'email':
            if (field.value && !isValidEmail(field.value)) {
                isValid = false;
                errorMessage = 'Por favor, insira um e-mail válido.';
            }
            break;
            
        case 'message':
            if (field.value && field.value.length > 1000) {
                isValid = false;
                errorMessage = 'A mensagem deve ter no máximo 1000 caracteres.';
            }
            break;
    }
    
    // Mostrar erro se inválido
    if (!isValid) {
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

// Mostrar erro no campo
function showFieldError(field, message) {
    const formGroup = field.closest('.form-group');
    formGroup.classList.add('error');
    
    let errorElement = formGroup.querySelector('.error-message');
    if (!errorElement) {
        errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        formGroup.appendChild(errorElement);
    }
    
    errorElement.textContent = message;
}

// Limpar erro do campo
function clearFieldError(field) {
    const formGroup = field.closest('.form-group');
    formGroup.classList.remove('error');
    
    const errorElement = formGroup.querySelector('.error-message');
    if (errorElement) {
        errorElement.style.display = 'none';
    }
}

// Validar e-mail
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Simular envio do formulário
async function simulateFormSubmission() {
    // Em produção, aqui seria feita a requisição para o servidor
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve();
        }, 2000);
    });
}

// Mostrar mensagem de sucesso
function showSuccessMessage() {
    const successMessage = document.getElementById('successMessage');
    if (successMessage) {
        successMessage.classList.add('active');
        
        // Auto-fechar após 5 segundos
        setTimeout(() => {
            closeSuccessMessage();
        }, 5000);
    }
}

// Fechar mensagem de sucesso
function closeSuccessMessage() {
    const successMessage = document.getElementById('successMessage');
    if (successMessage) {
        successMessage.classList.remove('active');
    }
}

// Inicializar FAQ
function initFAQ() {
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            toggleFAQ(this);
        });
    });
}

// Toggle FAQ item
function toggleFAQ(button) {
    const faqItem = button.closest('.faq-item');
    const answer = faqItem.querySelector('.faq-answer');
    const isExpanded = button.getAttribute('aria-expanded') === 'true';
    
    // Fechar todas as outras FAQs
    const allQuestions = document.querySelectorAll('.faq-question');
    const allAnswers = document.querySelectorAll('.faq-answer');
    
    allQuestions.forEach(q => q.setAttribute('aria-expanded', 'false'));
    allAnswers.forEach(a => a.classList.remove('active'));
    
    // Toggle atual
    if (!isExpanded) {
        button.setAttribute('aria-expanded', 'true');
        answer.classList.add('active');
    }
}

// Contador de caracteres
function initCharacterCounter() {
    const messageField = document.getElementById('message');
    const charCount = document.getElementById('messageCount');
    
    if (messageField && charCount) {
        messageField.addEventListener('input', updateCharacterCounter);
        updateCharacterCounter(); // Inicializar contador
    }
}

function updateCharacterCounter() {
    const messageField = document.getElementById('message');
    const charCount = document.getElementById('messageCount');
    
    if (messageField && charCount) {
        const currentLength = messageField.value.length;
        const maxLength = 1000;
        
        charCount.textContent = currentLength;
        
        // Mudar cor quando próximo do limite
        if (currentLength > maxLength * 0.9) {
            charCount.style.color = '#ef4444';
        } else if (currentLength > maxLength * 0.8) {
            charCount.style.color = '#f59e0b';
        } else {
            charCount.style.color = '';
        }
        
        // Validar se excedeu o limite
        if (currentLength > maxLength) {
            messageField.value = messageField.value.substring(0, maxLength);
            charCount.textContent = maxLength;
        }
    }
}

// Funcionalidades adicionais para melhorar UX
const ContactEnhancements = {
    init: function() {
        this.addFormAutoSave();
        this.addKeyboardShortcuts();
        this.addFormProgress();
    },
    
    // Auto-salvar formulário no localStorage
    addFormAutoSave: function() {
        const form = document.getElementById('contactForm');
        if (!form) return;
        
        const inputs = form.querySelectorAll('input, select, textarea');
        
        // Carregar dados salvos
        inputs.forEach(input => {
            const savedValue = localStorage.getItem(`contact_form_${input.name}`);
            if (savedValue && input.type !== 'checkbox') {
                input.value = savedValue;
            } else if (savedValue && input.type === 'checkbox') {
                input.checked = savedValue === 'true';
            }
        });
        
        // Salvar dados ao digitar
        inputs.forEach(input => {
            input.addEventListener('input', () => {
                if (input.type === 'checkbox') {
                    localStorage.setItem(`contact_form_${input.name}`, input.checked);
                } else {
                    localStorage.setItem(`contact_form_${input.name}`, input.value);
                }
            });
        });
        
        // Limpar dados salvos após envio bem-sucedido
        form.addEventListener('submit', () => {
            setTimeout(() => {
                inputs.forEach(input => {
                    localStorage.removeItem(`contact_form_${input.name}`);
                });
            }, 3000);
        });
    },
    
    // Atalhos de teclado
    addKeyboardShortcuts: function() {
        document.addEventListener('keydown', (e) => {
            // Ctrl/Cmd + Enter para enviar formulário
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                const form = document.getElementById('contactForm');
                if (form && document.activeElement && form.contains(document.activeElement)) {
                    e.preventDefault();
                    form.dispatchEvent(new Event('submit'));
                }
            }
            
            // Escape para fechar mensagem de sucesso
            if (e.key === 'Escape') {
                closeSuccessMessage();
            }
        });
    },
    
    // Indicador de progresso do formulário
    addFormProgress: function() {
        const form = document.getElementById('contactForm');
        if (!form) return;
        
        const requiredFields = form.querySelectorAll('[required]');
        const progressBar = document.createElement('div');
        progressBar.className = 'form-progress';
        progressBar.style.cssText = `
            height: 4px;
            background: var(--border-color);
            border-radius: 2px;
            margin-bottom: 2rem;
            overflow: hidden;
        `;
        
        const progressFill = document.createElement('div');
        progressFill.style.cssText = `
            height: 100%;
            background: var(--gradient);
            width: 0%;
            transition: width 0.3s ease;
        `;
        
        progressBar.appendChild(progressFill);
        form.insertBefore(progressBar, form.firstChild);
        
        // Atualizar progresso
        const updateProgress = () => {
            const filledFields = Array.from(requiredFields).filter(field => {
                return field.value.trim() !== '';
            });
            
            const progress = (filledFields.length / requiredFields.length) * 100;
            progressFill.style.width = progress + '%';
        };
        
        requiredFields.forEach(field => {
            field.addEventListener('input', updateProgress);
        });
        
        updateProgress(); // Inicializar
    }
};

// Inicializar melhorias quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('contactForm')) {
        ContactEnhancements.init();
    }
});

// Exportar funções globalmente
window.toggleFAQ = toggleFAQ;
window.closeSuccessMessage = closeSuccessMessage;
