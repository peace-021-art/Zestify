import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update the auth-login-btn to open modal instead of toggling directly
old_btn = """                <!-- User Profile (Logged Out State) -->
                <button id="auth-login-btn" onclick="toggleLoginState()" class="hidden sm:flex items-center gap-2 text-gray-600 hover:text-[#d94a11] hover:bg-gray-50 transition p-1 pr-3 rounded-full border border-transparent hover:border-gray-200">"""

new_btn = """                <!-- User Profile (Logged Out State) -->
                <button id="auth-login-btn" onclick="openAuthModal()" class="hidden sm:flex items-center gap-2 text-gray-600 hover:text-[#d94a11] hover:bg-gray-50 transition p-1 pr-3 rounded-full border border-transparent hover:border-gray-200">"""

content = content.replace(old_btn, new_btn)

# 2. Update the Log out button to use logoutUser
old_logout = """                            <a href="#" onclick="toggleLoginState(event)" class="flex items-center gap-3 px-3 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg transition font-bold">
                                <i class="fa-solid fa-arrow-right-from-bracket w-4 text-center"></i> Log out
                            </a>"""

new_logout = """                            <a href="#" onclick="logoutUser(event)" class="flex items-center gap-3 px-3 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg transition font-bold">
                                <i class="fa-solid fa-arrow-right-from-bracket w-4 text-center"></i> Log out
                            </a>"""

content = content.replace(old_logout, new_logout)

# 3. Add the Modal HTML right before closing </body>
modal_html = """
    <!-- Authentication Modal -->
    <div id="auth-modal" class="fixed inset-0 z-[100] flex items-center justify-center hidden">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm transition-opacity" onclick="closeAuthModal()"></div>
        
        <!-- Modal Content -->
        <div class="relative bg-white rounded-3xl shadow-2xl w-full max-w-md overflow-hidden transform scale-95 opacity-0 transition-all duration-300" id="auth-modal-content">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-gray-50 text-gray-500 hover:bg-gray-100 hover:text-gray-900 transition-colors z-10">
                <i class="fa-solid fa-xmark"></i>
            </button>
            
            <div class="p-8 sm:p-10 relative">
                <!-- Decoration -->
                <div class="absolute -top-20 -right-20 w-40 h-40 bg-[#ffb05c]/20 rounded-full blur-3xl"></div>
                <div class="absolute bottom-0 left-0 w-32 h-32 bg-green-200/20 rounded-full blur-3xl"></div>
                
                <div class="relative z-10">
                    <div class="w-12 h-12 bg-gray-900 rounded-xl flex items-center justify-center mb-6 shadow-md">
                        <i class="fa-solid fa-leaf text-white text-xl"></i>
                    </div>
                    
                    <h2 class="text-2xl font-black text-gray-900 mb-2">Welcome back</h2>
                    <p class="text-gray-500 text-sm font-medium mb-8">Please enter your details to sign in.</p>
                    
                    <form onsubmit="handleLoginSubmit(event)" class="space-y-4">
                        <div>
                            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-2">Email</label>
                            <input type="email" value="ayman@example.com" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#d94a11]/20 focus:border-[#d94a11] transition-all font-medium" required>
                        </div>
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider">Password</label>
                                <a href="#" class="text-xs font-bold text-[#d94a11] hover:underline">Forgot password?</a>
                            </div>
                            <input type="password" value="password123" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#d94a11]/20 focus:border-[#d94a11] transition-all font-medium" required>
                        </div>
                        
                        <div class="pt-2">
                            <button type="submit" class="w-full bg-gray-900 hover:bg-black text-white font-bold py-3.5 rounded-xl shadow-md transition-all hover:-translate-y-0.5">
                                Sign In
                            </button>
                        </div>
                    </form>
                    
                    <p class="text-center text-sm font-medium text-gray-500 mt-6">
                        Don't have an account? <a href="#" class="text-[#d94a11] font-bold hover:underline">Sign up</a>
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- Agentation Web Component -->
"""
content = content.replace('    <!-- Agentation Web Component -->', modal_html)

# 4. Replace toggleLoginState JS with the Modal JS logic
old_js = """        // Authentication State Logic
        function toggleLoginState(e) {
            if(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const loginBtn = document.getElementById('auth-login-btn');
            const userDropdown = document.getElementById('auth-user-dropdown');
            
            if(!loginBtn || !userDropdown) return;
            
            if(loginBtn.classList.contains('hidden')) {
                // Currently logged in -> Switch to Logged Out
                loginBtn.classList.remove('hidden');
                loginBtn.classList.add('sm:flex');
                
                userDropdown.classList.remove('sm:flex');
                userDropdown.classList.add('hidden');
            } else {
                // Currently logged out -> Switch to Logged In
                loginBtn.classList.remove('sm:flex');
                loginBtn.classList.add('hidden');
                
                userDropdown.classList.remove('hidden');
                userDropdown.classList.add('sm:flex');
            }
        }"""

new_js = """        // Authentication State Logic
        function openAuthModal() {
            const modal = document.getElementById('auth-modal');
            const content = document.getElementById('auth-modal-content');
            if(!modal) return;
            modal.classList.remove('hidden');
            // Small delay to allow display block to apply before transition
            setTimeout(() => {
                content.classList.remove('scale-95', 'opacity-0');
                content.classList.add('scale-100', 'opacity-100');
            }, 10);
        }

        function closeAuthModal() {
            const modal = document.getElementById('auth-modal');
            const content = document.getElementById('auth-modal-content');
            if(!modal) return;
            content.classList.remove('scale-100', 'opacity-100');
            content.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300); // match duration-300
        }

        function handleLoginSubmit(e) {
            e.preventDefault();
            
            // Close modal
            closeAuthModal();
            
            // Switch to logged in state
            const loginBtn = document.getElementById('auth-login-btn');
            const userDropdown = document.getElementById('auth-user-dropdown');
            
            if(loginBtn && userDropdown) {
                loginBtn.classList.remove('sm:flex');
                loginBtn.classList.add('hidden');
                
                userDropdown.classList.remove('hidden');
                userDropdown.classList.add('sm:flex');
            }
        }

        function logoutUser(e) {
            if(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const loginBtn = document.getElementById('auth-login-btn');
            const userDropdown = document.getElementById('auth-user-dropdown');
            
            if(loginBtn && userDropdown) {
                loginBtn.classList.remove('hidden');
                loginBtn.classList.add('sm:flex');
                
                userDropdown.classList.remove('sm:flex');
                userDropdown.classList.add('hidden');
            }
        }"""

content = content.replace(old_js, new_js)

with open("index.html", "w") as f:
    f.write(content)

print("Applied login modal fix.")
