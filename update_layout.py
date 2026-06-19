import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Deals of the week cards
old_deals = """        <div class="mb-10 sm:mb-16">
            <h2 class="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-900 mb-6">Deals of the Week</h2>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6">
                <!-- Deal 1 -->
                <div class="bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl p-5 flex items-center justify-between border border-red-100 shadow-sm hover:shadow-md transition-shadow group cursor-pointer">
                    <div class="flex-1 pr-4">
                        <span class="bg-red-500 text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider mb-2 inline-block">Save 20%</span>
                        <h3 class="font-bold text-gray-900 text-base sm:text-lg mb-1 group-hover:text-red-600 transition-colors line-clamp-2">Farm Fresh Strawberries</h3>
                        <div class="flex items-center gap-2 mt-2">
                            <span class="text-xl font-bold text-gray-900">₹269</span>
                            <span class="text-sm text-gray-400 line-through">₹338</span>
                        </div>
                    </div>
                    <div class="w-24 h-24 sm:w-32 sm:h-32 shrink-0 bg-white/60 rounded-full flex items-center justify-center overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1464965911861-746a04b4bca6?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Strawberries" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    </div>
                </div>

                <!-- Deal 2 -->
                <div class="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-5 flex items-center justify-between border border-green-100 shadow-sm hover:shadow-md transition-shadow group cursor-pointer">
                    <div class="flex-1 pr-4">
                        <span class="bg-green-500 text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider mb-2 inline-block">BOGO Free</span>
                        <h3 class="font-bold text-gray-900 text-base sm:text-lg mb-1 group-hover:text-green-600 transition-colors line-clamp-2">Organic Vine Tomatoes</h3>
                        <div class="flex items-center gap-2 mt-2">
                            <span class="text-xl font-bold text-gray-900">₹120</span>
                            <span class="text-sm text-green-600 font-bold bg-green-100 px-2 py-0.5 rounded">2 for 1</span>
                        </div>
                    </div>
                    <div class="w-24 h-24 sm:w-32 sm:h-32 shrink-0 bg-white/60 rounded-full flex items-center justify-center overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1596199050105-6d5d32222916?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Tomatoes" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    </div>
                </div>

                <!-- Deal 3 -->
                <div class="bg-gradient-to-br from-amber-50 to-yellow-50 rounded-2xl p-5 flex items-center justify-between border border-amber-100 shadow-sm hover:shadow-md transition-shadow group cursor-pointer">
                    <div class="flex-1 pr-4">
                        <span class="bg-amber-500 text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider mb-2 inline-block">Fresh Baked</span>
                        <h3 class="font-bold text-gray-900 text-base sm:text-lg mb-1 group-hover:text-amber-600 transition-colors line-clamp-2">Artisan Sourdough Bread</h3>
                        <div class="flex items-center gap-2 mt-2">
                            <span class="text-xl font-bold text-gray-900">₹162</span>
                            <span class="text-sm text-amber-600"><i class="fa-solid fa-fire"></i> Hot</span>
                        </div>
                    </div>
                    <div class="w-24 h-24 sm:w-32 sm:h-32 shrink-0 bg-white/60 rounded-full flex items-center justify-center overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1549931319-a545dcf3bc73?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" alt="Bread" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500">
                    </div>
                </div>
            </div>"""

new_deals = """        <div class="mb-10 sm:mb-16">
            <h2 class="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-900 mb-6 flex items-center justify-between">Deals of the Week <a href="#" class="text-sm font-bold text-[#d94a11] hover:underline">View All</a></h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">
                <!-- Deal 1 -->
                <div class="bg-white rounded-[2rem] overflow-hidden border border-gray-100 shadow-sm hover:shadow-xl transition-all group flex flex-col cursor-pointer relative">
                    <div class="absolute top-4 left-4 z-10 bg-red-500 text-white text-xs font-bold px-3 py-1.5 rounded-full uppercase tracking-widest shadow-md">Save 20%</div>
                    <div class="h-48 sm:h-56 bg-gray-50 flex items-center justify-center p-6 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1464965911861-746a04b4bca6?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Strawberries" class="w-full h-full object-cover rounded-xl transform group-hover:scale-105 transition-transform duration-500 shadow-sm">
                    </div>
                    <div class="p-6 sm:p-8 flex flex-col flex-1">
                        <h3 class="font-bold text-gray-900 text-lg sm:text-xl mb-2 group-hover:text-[#d94a11] transition-colors">Farm Fresh Strawberries</h3>
                        <p class="text-gray-500 text-sm mb-4 line-clamp-2">Sweet, juicy, and perfectly ripe strawberries from local organic farms.</p>
                        <div class="flex items-center justify-between mt-auto">
                            <div class="flex items-center gap-3">
                                <span class="text-2xl font-black text-gray-900">₹269</span>
                                <span class="text-sm text-gray-400 line-through font-medium">₹338</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Deal 2 -->
                <div class="bg-white rounded-[2rem] overflow-hidden border border-gray-100 shadow-sm hover:shadow-xl transition-all group flex flex-col cursor-pointer relative">
                    <div class="absolute top-4 left-4 z-10 bg-green-500 text-white text-xs font-bold px-3 py-1.5 rounded-full uppercase tracking-widest shadow-md">BOGO Free</div>
                    <div class="h-48 sm:h-56 bg-gray-50 flex items-center justify-center p-6 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1596199050105-6d5d32222916?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Tomatoes" class="w-full h-full object-cover rounded-xl transform group-hover:scale-105 transition-transform duration-500 shadow-sm">
                    </div>
                    <div class="p-6 sm:p-8 flex flex-col flex-1">
                        <h3 class="font-bold text-gray-900 text-lg sm:text-xl mb-2 group-hover:text-[#d94a11] transition-colors">Organic Vine Tomatoes</h3>
                        <p class="text-gray-500 text-sm mb-4 line-clamp-2">Rich, flavorful tomatoes still on the vine. Perfect for salads and sauces.</p>
                        <div class="flex items-center justify-between mt-auto">
                            <div class="flex items-center gap-3">
                                <span class="text-2xl font-black text-gray-900">₹120</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Deal 3 -->
                <div class="bg-white rounded-[2rem] overflow-hidden border border-gray-100 shadow-sm hover:shadow-xl transition-all group flex flex-col cursor-pointer relative">
                    <div class="absolute top-4 left-4 z-10 bg-[#d94a11] text-white text-xs font-bold px-3 py-1.5 rounded-full uppercase tracking-widest shadow-md">Fresh Baked</div>
                    <div class="h-48 sm:h-56 bg-gray-50 flex items-center justify-center p-6 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1549931319-a545dcf3bc73?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Bread" class="w-full h-full object-cover rounded-xl transform group-hover:scale-105 transition-transform duration-500 shadow-sm">
                    </div>
                    <div class="p-6 sm:p-8 flex flex-col flex-1">
                        <h3 class="font-bold text-gray-900 text-lg sm:text-xl mb-2 group-hover:text-[#d94a11] transition-colors">Artisan Sourdough Bread</h3>
                        <p class="text-gray-500 text-sm mb-4 line-clamp-2">Crispy crust with a soft, chewy interior. Baked fresh every morning.</p>
                        <div class="flex items-center justify-between mt-auto">
                            <div class="flex items-center gap-3">
                                <span class="text-2xl font-black text-gray-900">₹162</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

if old_deals in content:
    content = content.replace(old_deals, new_deals)
else:
    print("Warning: old_deals not found")

# 2. Improve the `bg-gradient-to-l` element
old_banner_2 = """        <div class="bg-gradient-to-l from-[#fff7ed] to-[#bbf7d0] border border-[#bbf7d0] rounded-2xl sm:rounded-[3rem] p-8 sm:p-12 lg:p-16 flex flex-col md:flex-row-reverse items-center justify-between overflow-hidden relative shadow-sm mb-20 lg:mb-24 group gap-10">
            <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] mix-blend-overlay"></div>
            
            <div class="relative z-10 text-center md:text-left md:w-1/2 md:pl-10">
                <span class="bg-[#d94a11] text-white text-xs sm:text-sm font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-6 inline-block shadow-md">Farm to Table</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-gray-900 mb-6 leading-tight">Fresh harvest<br>from <span class="text-green-600">local farms.</span></h2>
                <p class="text-gray-600 text-base sm:text-lg max-w-lg mx-auto md:mx-0 font-medium leading-relaxed mb-8">We partner directly with local farmers to bring you the freshest, most nutrient-dense produce within hours of harvesting.</p>
                
                <button class="bg-[#d94a11] hover:bg-[#9c2b03] text-white font-bold py-3.5 px-8 rounded-full shadow-[0_8px_20px_rgba(217,74,17,0.3)] flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 mx-auto md:mx-0">
                    Meet Our Farmers <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>

            <div class="w-full md:w-1/2 relative flex justify-center items-center shrink-0">
                <div class="relative w-64 h-64 sm:w-80 sm:h-80 lg:w-96 lg:h-96">
                    <div class="absolute inset-0 bg-[#d94a11]/10 rounded-full blur-2xl animate-pulse"></div>
                    <img src="https://images.unsplash.com/photo-1566385101042-1a0aa0c1268c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Fresh Vegetables" class="relative z-10 w-full h-full object-cover rounded-full shadow-2xl border-4 border-white transform group-hover:-rotate-6 transition-transform duration-700">
                    
                    <!-- Floating Badge -->
                    <div class="absolute -top-6 -right-6 bg-white p-4 rounded-2xl shadow-xl z-20 border border-gray-50 transform rotate-6 animate-bounce" style="animation-duration: 3.5s;">
                        <span class="font-bold text-[#d94a11] text-sm sm:text-base flex items-center gap-2"><div class="w-8 h-8 rounded-full bg-[#bbf7d0] flex items-center justify-center"><i class="fa-solid fa-leaf text-[#d94a11]"></i></div> 100% Fresh</span>
                    </div>
                </div>
            </div>
        </div>"""

new_banner_2 = """        <div class="bg-gray-900 rounded-[2rem] sm:rounded-[3rem] p-8 sm:p-12 lg:p-16 flex flex-col md:flex-row-reverse items-center justify-between overflow-hidden relative shadow-xl mb-20 lg:mb-24 group gap-10">
            <div class="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] mix-blend-overlay"></div>
            
            <div class="relative z-10 text-center md:text-left md:w-1/2 md:pl-10">
                <span class="bg-white/10 text-white text-xs sm:text-sm font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-6 inline-block border border-white/20">Farm to Table</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6 leading-tight">Fresh harvest<br>from <span class="text-[#ffb05c]">local farms.</span></h2>
                <p class="text-gray-300 text-base sm:text-lg max-w-lg mx-auto md:mx-0 font-medium leading-relaxed mb-8">We partner directly with local farmers to bring you the freshest, most nutrient-dense produce within hours of harvesting.</p>
                
                <button class="bg-white hover:bg-gray-100 text-gray-900 font-bold py-3.5 px-8 rounded-full shadow-lg flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 mx-auto md:mx-0">
                    Meet Our Farmers <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>

            <div class="w-full md:w-1/2 relative flex justify-center items-center shrink-0">
                <div class="relative w-64 h-64 sm:w-80 sm:h-80 lg:w-96 lg:h-96">
                    <img src="https://images.unsplash.com/photo-1566385101042-1a0aa0c1268c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Fresh Vegetables" class="relative z-10 w-full h-full object-cover rounded-[2rem] shadow-2xl border border-white/10 transform group-hover:scale-105 transition-transform duration-700">
                    
                    <!-- Floating Badge -->
                    <div class="absolute -bottom-6 -right-6 bg-white p-4 rounded-2xl shadow-xl z-20 border border-gray-100 flex items-center gap-4 animate-bounce" style="animation-duration: 4s;">
                        <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center shrink-0"><i class="fa-solid fa-leaf text-green-600 text-xl"></i></div>
                        <div>
                            <p class="text-xs text-gray-500 font-bold uppercase tracking-wider">Quality</p>
                            <p class="font-black text-gray-900">100% Organic</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""

if old_banner_2 in content:
    content = content.replace(old_banner_2, new_banner_2)
else:
    print("Warning: old_banner_2 not found")

# 3 & 7. Fix ₹203 text size and banner color pattern
old_banner_1 = """        <div class="bg-[#d94a11] rounded-2xl sm:rounded-[2rem] p-8 sm:p-10 lg:p-14 flex flex-col md:flex-row items-center justify-between overflow-hidden relative shadow-lg mb-20 group">
            <div class="absolute -right-20 -top-20 w-80 h-80 bg-[#ffb05c]/20 rounded-full blur-3xl transform group-hover:scale-110 transition-transform duration-700"></div>
            <div class="absolute -left-10 -bottom-10 w-64 h-64 bg-yellow-400/20 rounded-full blur-3xl transform group-hover:scale-110 transition-transform duration-700"></div>
            
            <div class="relative z-10 text-center md:text-left mb-8 md:mb-0 md:pr-10">
                <span class="bg-[#ffb05c] text-[#d94a11] text-xs sm:text-sm font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-4 inline-block shadow-sm">Special Reward</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-4 leading-tight">GET 10% CASHBACK<br>ON SHOPPING <span class="text-yellow-400">₹203</span></h2>
                <p class="text-green-100 text-base sm:text-lg max-w-lg mx-auto md:mx-0 font-medium">Shopping is a bit of a relaxing hobby for me, which is sometimes troubling for the bank balance.</p>
            </div>
            
            <div class="relative z-10 flex flex-col sm:flex-row gap-4 shrink-0">
                <button class="bg-[#ffb05c] hover:bg-white text-[#d94a11] font-bold py-4 px-8 rounded-full shadow-xl flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 text-lg">
                    Learn More <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>"""

new_banner_1 = """        <div class="bg-gradient-to-r from-gray-50 to-gray-100 border border-gray-200 rounded-2xl sm:rounded-[3rem] p-8 sm:p-12 lg:p-16 flex flex-col md:flex-row items-center justify-between relative shadow-sm mb-20 group">
            <div class="relative z-10 text-center md:text-left mb-8 md:mb-0 md:pr-10">
                <span class="bg-[#d94a11]/10 text-[#d94a11] text-xs sm:text-sm font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-6 inline-block">Special Reward</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-extrabold text-gray-900 mb-6 leading-tight">GET 10% CASHBACK<br>ON SHOPPING <span class="text-[#d94a11] text-5xl sm:text-6xl lg:text-8xl block mt-2">₹203</span></h2>
                <p class="text-gray-600 text-base sm:text-lg max-w-lg mx-auto md:mx-0 font-medium">Earn immediate cashback on your daily grocery shopping. Use it on your next purchase!</p>
            </div>
            
            <div class="relative z-10 flex flex-col sm:flex-row gap-4 shrink-0">
                <button class="bg-gray-900 hover:bg-black text-white font-bold py-4 px-10 rounded-full shadow-lg flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 text-lg">
                    Claim Reward <i class="fa-solid fa-gift"></i>
                </button>
            </div>
        </div>"""

if old_banner_1 in content:
    content = content.replace(old_banner_1, new_banner_1)
else:
    print("Warning: old_banner_1 not found")

# 4. Improve "Special Offer" color effect
content = content.replace(
    '<span class="inline-block bg-white/20 text-[#ffb05c] text-xs font-bold px-3 py-1 rounded-full mb-4 backdrop-blur-sm border border-white/10 uppercase tracking-wider">Special Offer</span>',
    '<span class="inline-block bg-gradient-to-r from-[#d94a11] to-[#bd3b0a] text-white text-xs font-bold px-4 py-1.5 rounded-full mb-4 uppercase tracking-widest shadow-lg">Special Offer</span>'
)

# 5. Subscribe text to white/professional
content = content.replace(
    '<p class="text-[#ffb05c] text-sm sm:text-base font-medium opacity-90 max-w-md mx-auto lg:mx-0">Subscribe to get up to 20% OFF on your first purchase and receive daily fresh food updates.</p>',
    '<p class="text-gray-300 text-sm sm:text-base font-medium opacity-90 max-w-md mx-auto lg:mx-0">Subscribe to get up to 20% OFF on your first purchase and receive daily fresh food updates.</p>'
)

# 6. Fix footer section responsive
content = content.replace(
    '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-8 lg:gap-10 mb-16">',
    '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 lg:gap-10 mb-16">'
)

with open("index.html", "w") as f:
    f.write(content)

print("Applied all feedback updates.")
