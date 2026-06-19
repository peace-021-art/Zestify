import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Remove language dropdown
lang_dropdown = """                <div class="relative group cursor-pointer">
                    <div class="flex items-center gap-1.5 p-2 text-gray-700 hover:text-[#d94a11] transition">
                        <i class="fa-solid fa-globe text-sm"></i>
                        <span class="text-sm font-bold">EN</span>
                        <i class="fa-solid fa-chevron-down text-[10px] text-gray-400 group-hover:rotate-180 transition-transform"></i>
                    </div>
                    <!-- Dropdown -->
                    <div class="absolute right-0 top-full mt-2 w-32 bg-white rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50 transform origin-top scale-95 group-hover:scale-100 py-2 border border-gray-100">
                        <a href="#" class="block px-4 py-2 text-sm text-[#d94a11] font-bold bg-[#fff7ed]">English</a>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-600 hover:bg-[#fff7ed] hover:text-[#d94a11]">Hindi</a>
                    </div>
                </div>"""

if lang_dropdown in content:
    content = content.replace(lang_dropdown, "")
else:
    print("Warning: lang_dropdown not found")

# 2. Change Zestify text color
old_logo = """    <span class="text-2xl font-black text-[#d94a11] tracking-tight">Zestify</span>"""
new_logo = """    <span class="text-2xl font-black text-gray-900 tracking-tight">Zestify</span>"""

if old_logo in content:
    content = content.replace(old_logo, new_logo)
else:
    print("Warning: old_logo not found")

# 3. Fix the last w-8 button
old_button_2 = """                        <button class="w-8 h-8 rounded-full bg-[#d94a11] text-white flex items-center justify-center transition-colors shadow-sm">
                            <i class="fa-solid fa-check"></i>
                        </button>"""
new_button_2 = """                        <button class="px-4 py-1.5 rounded-full bg-white border border-gray-200 text-gray-900 text-xs sm:text-sm font-bold flex items-center gap-1.5 hover:bg-gray-900 hover:text-white hover:border-gray-900 transition-all shadow-sm transform hover:-translate-y-0.5">
                            <i class="fa-solid fa-plus text-[10px]"></i> Add
                        </button>"""

if old_button_2 in content:
    content = content.replace(old_button_2, new_button_2)
else:
    print("Warning: old_button_2 not found")


with open("index.html", "w") as f:
    f.write(content)

print("Applied final fixes.")
