import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update HTML structure
old_dropdown_start = """                <!-- User Profile Dropdown -->
                <div class="relative group hidden sm:flex cursor-pointer z-[60]">"""

new_dropdown_start = """                <!-- User Profile (Logged Out State) -->
                <button id="auth-login-btn" onclick="toggleLoginState()" class="hidden sm:flex items-center gap-2 text-gray-600 hover:text-[#d94a11] hover:bg-gray-50 transition p-1 pr-3 rounded-full border border-transparent hover:border-gray-200">
                    <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 shadow-sm border border-gray-200">
                        <i class="fa-regular fa-user"></i>
                    </div>
                    <span class="text-sm font-bold hidden xl:block mr-1">Sign In</span>
                </button>

                <!-- User Profile Dropdown (Logged In State) -->
                <div id="auth-user-dropdown" class="relative group hidden cursor-pointer z-[60]">"""

content = content.replace(old_dropdown_start, new_dropdown_start)

# Add onclick to Log out
old_logout = """                            <a href="#" class="flex items-center gap-3 px-3 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg transition font-bold">
                                <i class="fa-solid fa-arrow-right-from-bracket w-4 text-center"></i> Log out
                            </a>"""

new_logout = """                            <a href="#" onclick="toggleLoginState(event)" class="flex items-center gap-3 px-3 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg transition font-bold">
                                <i class="fa-solid fa-arrow-right-from-bracket w-4 text-center"></i> Log out
                            </a>"""

content = content.replace(old_logout, new_logout)

# 2. Add Javascript function at the end
old_js_end = """        // Initialize Products Add to Cart Logic"""

new_js_end = """        // Authentication State Logic
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
        }

        // Initialize Products Add to Cart Logic"""

content = content.replace(old_js_end, new_js_end)

with open("index.html", "w") as f:
    f.write(content)

print("Applied login state fix.")
