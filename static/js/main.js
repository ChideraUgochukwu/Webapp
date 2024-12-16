// WebSocket Connection
class ChatWebSocket {
    constructor(roomId) {
        this.roomId = roomId;
        this.socket = null;
        this.messageContainer = document.querySelector('.chat-messages');
        this.messageForm = document.querySelector('#message-form');
        this.messageInput = document.querySelector('#message-input');
    }

    connect() {
        this.socket = new WebSocket(
            `${window.location.protocol === 'https:' ? 'wss:' : 'ws:'}//${window.location.host}/ws/chat/${this.roomId}/`
        );

        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.appendMessage(data);
        };

        this.socket.onclose = () => {
            console.log('WebSocket disconnected');
            // Attempt to reconnect after 2 seconds
            setTimeout(() => this.connect(), 2000);
        };

        if (this.messageForm) {
            this.messageForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.sendMessage();
            });
        }
    }

    sendMessage() {
        const message = this.messageInput.value.trim();
        if (message && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(JSON.stringify({
                'message': message
            }));
            this.messageInput.value = '';
        }
    }

    appendMessage(data) {
        if (!this.messageContainer) return;

        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', 'fade-in');
        
        if (data.user === currentUser) {
            messageDiv.classList.add('message-own');
        } else {
            messageDiv.classList.add('message-other');
        }

        messageDiv.innerHTML = `
            <div class="message-content">${data.message}</div>
            <div class="message-info">
                ${data.user} - ${new Date(data.timestamp).toLocaleTimeString()}
            </div>
        `;

        this.messageContainer.appendChild(messageDiv);
        this.messageContainer.scrollTop = this.messageContainer.scrollHeight;
    }
}

// Initialize tooltips and popovers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize Bootstrap popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Initialize chat if we're on a chat page
    const chatRoom = document.querySelector('[data-room-id]');
    if (chatRoom) {
        const roomId = chatRoom.dataset.roomId;
        const chat = new ChatWebSocket(roomId);
        chat.connect();
    }
});

// Search functionality
const searchForm = document.querySelector('#search-form');
if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
        const searchInput = this.querySelector('input[type="search"]');
        if (!searchInput.value.trim()) {
            e.preventDefault();
        }
    });
}

// Profile image preview
const avatarInput = document.querySelector('#avatar-input');
const avatarPreview = document.querySelector('#avatar-preview');
if (avatarInput && avatarPreview) {
    avatarInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                avatarPreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
}

// Responsive navigation
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');
if (navbarToggler && navbarCollapse) {
    document.addEventListener('click', function(e) {
        if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target) && navbarCollapse.classList.contains('show')) {
            navbarToggler.click();
        }
    });
}
