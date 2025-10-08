// JavaScript para funcionalidades da página de documentação

document.addEventListener('DOMContentLoaded', function() {
    initDocsNavigation();
    initCopyButtons();
    initSmoothScrolling();
});

// Navegação da documentação
function initDocsNavigation() {
    const navLinks = document.querySelectorAll('.docs-nav-link');
    const sections = document.querySelectorAll('.docs-section');
    
    if (!navLinks.length || !sections.length) return;
    
    // Highlight da seção atual baseada no scroll
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;
                    
                    // Remove active de todos os links
                    navLinks.forEach(link => link.classList.remove('active'));
                    
                    // Adiciona active ao link correspondente
                    const activeLink = document.querySelector(`[href="#${id}"]`);
                    if (activeLink) {
                        activeLink.classList.add('active');
                    }
                }
            });
        },
        {
            rootMargin: '-120px 0px -50% 0px',
            threshold: 0.1
        }
    );
    
    sections.forEach(section => observer.observe(section));
    
    // Click nos links de navegação
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL without triggering scroll
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });
    
    // Highlight inicial baseado na URL
    const hash = window.location.hash;
    if (hash) {
        const activeLink = document.querySelector(`[href="${hash}"]`);
        if (activeLink) {
            navLinks.forEach(link => link.classList.remove('active'));
            activeLink.classList.add('active');
        }
    }
}

// Botões de copiar código
function initCopyButtons() {
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const codeBlock = this.parentElement;
            const code = codeBlock.querySelector('code');
            
            if (code) {
                const text = code.textContent;
                const success = await copyToClipboard(text);
                
                if (success) {
                    // Feedback visual
                    const originalText = this.textContent;
                    this.textContent = 'Copiado!';
                    this.style.background = 'rgba(16, 185, 129, 0.2)';
                    this.style.borderColor = 'rgba(16, 185, 129, 0.3)';
                    
                    // Highlight do bloco de código
                    codeBlock.classList.add('copied');
                    
                    setTimeout(() => {
                        this.textContent = originalText;
                        this.style.background = '';
                        this.style.borderColor = '';
                        codeBlock.classList.remove('copied');
                    }, 2000);
                    
                    // Notificação
                    Utils.showNotification('Código copiado para a área de transferência!', 'success');
                } else {
                    Utils.showNotification('Erro ao copiar código', 'error');
                }
            }
        });
    });
}

// Função global para copiar texto (usada nos botões inline)
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        // Fallback para navegadores mais antigos
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {
            const successful = document.execCommand('copy');
            textArea.remove();
            return successful;
        } catch (err) {
            textArea.remove();
            return false;
        }
    }
}

// Smooth scrolling para links internos
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target && !this.classList.contains('docs-nav-link')) {
                e.preventDefault();
                
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL
                history.pushState(null, null, href);
            }
        });
    });
}

// Funcionalidades de busca (para implementação futura)
const DocsSearch = {
    init: function() {
        // Implementar busca na documentação
        // Por enquanto, apenas um placeholder
    },
    
    search: function(query) {
        // Implementar lógica de busca
        console.log('Buscando por:', query);
    }
};

// Funcionalidades para melhorar a experiência de leitura
const DocsEnhancements = {
    init: function() {
        this.addReadingProgress();
        this.addTableOfContents();
        this.addCodeLanguageLabels();
    },
    
    addReadingProgress: function() {
        // Barra de progresso de leitura
        const progressBar = document.createElement('div');
        progressBar.className = 'reading-progress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            z-index: 1001;
            transition: width 0.3s ease;
        `;
        
        document.body.appendChild(progressBar);
        
        window.addEventListener('scroll', () => {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = (window.scrollY / docHeight) * 100;
            progressBar.style.width = Math.min(scrolled, 100) + '%';
        });
    },
    
    addTableOfContents: function() {
        // Gerar índice automático baseado nos headings
        const headings = document.querySelectorAll('.docs-section h2, .docs-section h3');
        
        if (headings.length > 0) {
            // Esta funcionalidade pode ser expandida para gerar um TOC dinâmico
            console.log('Headings encontrados:', headings.length);
        }
    },
    
    addCodeLanguageLabels: function() {
        // Adicionar labels de linguagem aos blocos de código
        const codeBlocks = document.querySelectorAll('.code-block pre code[class*="language-"]');
        
        codeBlocks.forEach(code => {
            const className = code.className;
            const language = className.match(/language-(\w+)/);
            
            if (language) {
                const label = document.createElement('div');
                label.className = 'code-language-label';
                label.textContent = language[1].toUpperCase();
                label.style.cssText = `
                    position: absolute;
                    top: 1rem;
                    left: 1rem;
                    background: rgba(255, 255, 255, 0.1);
                    color: white;
                    padding: 0.25rem 0.75rem;
                    border-radius: 0.25rem;
                    font-size: 0.75rem;
                    font-weight: 500;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                `;
                
                const codeBlock = code.closest('.code-block');
                if (codeBlock) {
                    codeBlock.style.position = 'relative';
                    codeBlock.appendChild(label);
                }
            }
        });
    }
};

// Utilitários específicos para documentação
const DocsUtils = {
    // Gerar link permanente para seções
    generatePermalink: function(element) {
        const id = element.id;
        if (id) {
            const permalink = document.createElement('a');
            permalink.href = `#${id}`;
            permalink.className = 'permalink';
            permalink.innerHTML = '#';
            permalink.title = 'Link permanente para esta seção';
            permalink.style.cssText = `
                color: var(--text-light);
                text-decoration: none;
                margin-left: 0.5rem;
                opacity: 0;
                transition: opacity 0.3s ease;
            `;
            
            element.appendChild(permalink);
            
            element.addEventListener('mouseenter', () => {
                permalink.style.opacity = '1';
            });
            
            element.addEventListener('mouseleave', () => {
                permalink.style.opacity = '0';
            });
        }
    },
    
    // Destacar código mencionado no texto
    highlightInlineCode: function() {
        const inlineCode = document.querySelectorAll('p code, li code');
        
        inlineCode.forEach(code => {
            code.style.cssText = `
                background: rgba(59, 130, 246, 0.1);
                color: var(--primary-color);
                padding: 0.2rem 0.4rem;
                border-radius: 0.25rem;
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.875em;
                font-weight: 500;
            `;
        });
    }
};

// Inicializar melhorias quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.docs-main')) {
        DocsEnhancements.init();
        DocsUtils.highlightInlineCode();
        
        // Adicionar permalinks aos headings
        const headings = document.querySelectorAll('.docs-section h2[id], .docs-section h3[id]');
        headings.forEach(heading => {
            DocsUtils.generatePermalink(heading);
        });
    }
});

// Exportar funções globalmente para uso em outros scripts
window.copyToClipboard = copyToClipboard;
window.DocsSearch = DocsSearch;
window.DocsUtils = DocsUtils;
