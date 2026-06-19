import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update Veggies banner background and text colors
old_veggies = """        <!-- NEW: Vegetarian Section (Mirrored Split Layout) -->
        <div class="bg-gray-900 rounded-[2rem] sm:rounded-[3rem] p-8 sm:p-12 lg:p-16 flex flex-col md:flex-row-reverse items-center justify-between overflow-hidden relative shadow-xl mb-20 lg:mb-24 group gap-10">
            <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] mix-blend-overlay"></div>
            
            <div class="flex-1 max-w-2xl relative z-10 text-center md:text-left">
                <span class="bg-white/10 border border-white/20 text-white text-xs sm:text-sm font-bold px-5 py-2 rounded-full uppercase tracking-widest mb-6 inline-block relative overflow-hidden group">
                    <span class="relative z-10 drop-shadow-sm">Daily Fresh Harvest</span>
                </span>
                
                <h2 class="font-black text-white mb-8 leading-[1.05] tracking-tight">
                    <span class="block text-3xl sm:text-4xl lg:text-5xl text-gray-300 font-extrabold mb-1 tracking-normal">Organic & Healthy</span>
                    <span class="block text-6xl sm:text-7xl lg:text-[6.5rem] xl:text-[8rem] text-white drop-shadow-sm">Veggies</span>
                </h2>
                
                <p class="text-gray-300 text-lg sm:text-xl mb-8 leading-relaxed max-w-lg mx-auto md:mx-0">Boost your immunity with our farm-fresh, pesticide-free vegetables. Sourced directly from local farmers to bring you the best quality greens.</p>
                
                <button class="bg-white hover:bg-gray-200 text-gray-900 font-bold py-4 px-8 rounded-full shadow-lg flex items-center justify-center gap-2 transition-all hover:-translate-y-1 mx-auto md:mx-0 text-lg w-max">
                    Shop Vegetables <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>"""

new_veggies = """        <!-- NEW: Vegetarian Section (Mirrored Split Layout) -->
        <div class="bg-gradient-to-l from-emerald-50 to-teal-50 border border-emerald-100 rounded-[2rem] sm:rounded-[3rem] p-8 sm:p-12 lg:p-16 flex flex-col md:flex-row-reverse items-center justify-between overflow-hidden relative shadow-sm mb-20 lg:mb-24 group gap-10">
            <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-teal-200/30 rounded-full blur-2xl transform group-hover:scale-110 transition-transform duration-700"></div>
            
            <div class="flex-1 max-w-2xl relative z-10 text-center md:text-left">
                <span class="bg-white/50 backdrop-blur-md border border-white shadow-sm text-teal-700 text-xs sm:text-sm font-bold px-5 py-2 rounded-full uppercase tracking-widest mb-6 inline-block relative overflow-hidden group">
                    <span class="relative z-10 drop-shadow-sm">Daily Fresh Harvest</span>
                </span>
                
                <h2 class="font-black text-gray-900 mb-8 leading-[1.05] tracking-tight">
                    <span class="block text-3xl sm:text-4xl lg:text-5xl text-teal-700 font-extrabold mb-1 tracking-normal">Organic & Healthy</span>
                    <span class="block text-6xl sm:text-7xl lg:text-[6.5rem] xl:text-[8rem] text-teal-800 drop-shadow-sm">Veggies</span>
                </h2>
                
                <p class="text-gray-700 text-lg sm:text-xl mb-8 leading-relaxed max-w-lg mx-auto md:mx-0">Boost your immunity with our farm-fresh, pesticide-free vegetables. Sourced directly from local farmers to bring you the best quality greens.</p>
                
                <button class="bg-teal-700 hover:bg-teal-800 text-white font-bold py-4 px-8 rounded-full shadow-lg shadow-teal-700/30 flex items-center justify-center gap-2 transition-all hover:-translate-y-1 mx-auto md:mx-0 text-lg w-max">
                    Shop Vegetables <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>"""

if old_veggies in content:
    content = content.replace(old_veggies, new_veggies)
else:
    print("Warning: old_veggies not found")

# 2. Update Deal of the Week buttons
old_button = """                            <button class="w-10 h-10 rounded-full bg-gray-100 text-gray-900 hover:bg-gray-900 hover:text-white transition-colors flex items-center justify-center shadow-sm">
                                <i class="fa-solid fa-cart-plus"></i>
                            </button>"""

new_button = """                            <button class="px-4 py-1.5 rounded-full bg-white border border-gray-200 text-gray-900 text-xs sm:text-sm font-bold flex items-center gap-1.5 hover:bg-gray-900 hover:text-white hover:border-gray-900 transition-all shadow-sm transform hover:-translate-y-0.5">
                                <i class="fa-solid fa-plus text-[10px]"></i> Add
                            </button>"""

content = content.replace(old_button, new_button)

# 3. Update Browse Categories button
old_categories = """                <!-- Categories Button -->
                <button class="flex items-center gap-3 bg-gray-900 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-md hover:bg-black transition group shrink-0">
                    <i class="fa-solid fa-bars-staggered"></i>
                    Browse Categories
                    <i class="fa-solid fa-chevron-down text-[10px] text-white/70 group-hover:rotate-180 transition-transform ml-1"></i>
                </button>"""

new_categories = """                <!-- Categories Button with Dropdown -->
                <div class="relative group cursor-pointer z-50">
                    <button class="flex items-center gap-3 bg-gray-900 text-white px-5 py-2.5 rounded-full text-sm font-bold shadow-md group-hover:bg-black transition shrink-0 w-full justify-between">
                        <span class="flex items-center gap-3">
                            <i class="fa-solid fa-bars-staggered"></i>
                            Browse Categories
                        </span>
                        <i class="fa-solid fa-chevron-down text-[10px] text-white/70 group-hover:rotate-180 transition-transform ml-1"></i>
                    </button>
                    <!-- Mega Menu Dropdown -->
                    <div class="absolute left-0 top-full mt-2 w-64 bg-white rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.1)] border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform origin-top scale-95 group-hover:scale-100 py-3 font-medium overflow-hidden">
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-gray-700 hover:bg-gray-50 hover:text-[#d94a11] transition-colors"><i class="fa-solid fa-apple-whole w-5 text-center text-red-500"></i> Fresh Fruits</a>
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-gray-700 hover:bg-gray-50 hover:text-[#d94a11] transition-colors"><i class="fa-solid fa-carrot w-5 text-center text-orange-500"></i> Organic Veggies</a>
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-gray-700 hover:bg-gray-50 hover:text-[#d94a11] transition-colors"><i class="fa-solid fa-bread-slice w-5 text-center text-amber-600"></i> Artisan Breads</a>
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-gray-700 hover:bg-gray-50 hover:text-[#d94a11] transition-colors"><i class="fa-solid fa-cow w-5 text-center text-gray-500"></i> Farm Dairy</a>
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-gray-700 hover:bg-gray-50 hover:text-[#d94a11] transition-colors"><i class="fa-solid fa-seedling w-5 text-center text-green-600"></i> Herbs & Seasonings</a>
                        <div class="h-px bg-gray-100 my-2 mx-4"></div>
                        <a href="#" class="flex items-center gap-3 px-5 py-2.5 text-[#d94a11] hover:bg-orange-50 font-bold transition-colors">View All Categories <i class="fa-solid fa-arrow-right ml-auto text-xs"></i></a>
                    </div>
                </div>"""

if old_categories in content:
    content = content.replace(old_categories, new_categories)
else:
    print("Warning: old_categories not found")


with open("index.html", "w") as f:
    f.write(content)

print("Applied 3 fixes.")
