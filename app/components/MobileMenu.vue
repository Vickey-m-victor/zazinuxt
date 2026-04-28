<template>
    <!--==============================
    Mobile Menu
    ============================== -->
    <div class="vs-menu-wrapper">
        <div class="vs-menu-area text-center">
            <button class="vs-menu-toggle"><i class="fal fa-times"></i></button>
            <div class="mobile-logo">
                <NuxtLink to="/"><img src="/img/logo.svg" alt="Kiddino"></NuxtLink>
            </div>
            <div class="vs-mobile-menu">
                <ul>
                    <li><NuxtLink to="/">Home</NuxtLink></li>
                    <li><NuxtLink to="/about">About Us</NuxtLink></li>
                    <li><NuxtLink to="/class">Classes</NuxtLink></li>
                    <li><NuxtLink to="/blog">Blog</NuxtLink></li>
                    <li><NuxtLink to="/service">Services</NuxtLink></li>
                    <li><NuxtLink to="/contact">Contact Us</NuxtLink></li>
                </ul>
            </div>
        </div>
    </div>
</template>
