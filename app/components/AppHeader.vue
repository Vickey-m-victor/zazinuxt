<template>
    <!--==============================
        Header Area
    ==============================-->
    <header class="vs-header header-layout1">
        <div class="header-top">
            <div class="container">
                <div class="row justify-content-between align-items-center">
                    <div class="col-auto d-none d-lg-block">
                        <div class="header-links style-white">
                            <ul>
                                <li><NuxtLink to="/registration"><i class="far fa-user-circle"></i>Login & Register</NuxtLink>
                                </li>
                                <li><NuxtLink to="/contact" class="searchBoxTggler"><i class="far fa-search"></i>Search
                                        Keyword</NuxtLink></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-auto text-center">
                        <div class="header-links style2 style-white">
                            <ul>
                                <li><i class="fas fa-envelope"></i>Email: <NuxtLink
                                        href="mailto:user@example.com">user@example.com</NuxtLink></li>
                                <li><i class="fas fa-mobile-alt"></i>Phone: <NuxtLink href="tel:+4402076897888">+44 (0) 207 689
                                        7888</NuxtLink></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="sticky-wrap">
            <div class="sticky-active">
                <div class="container">
                    <div class="row gx-3 align-items-center justify-content-between">
                        <div class="col-8 col-sm-auto">
                            <div class="header-logo">
                                <NuxtLink to="/">
                                    <img src="/img/logo.svg" alt="logo">
                                </NuxtLink>
                            </div>
                        </div>
                        <div class="col text-end text-lg-center">
                            <nav class="main-menu menu-style1 d-none d-lg-block">
                                <ul>
                                    <li><NuxtLink to="/">Home</NuxtLink></li>
                                    <li><NuxtLink to="/about">About Us</NuxtLink></li>
                                    <li><NuxtLink to="/class">Classes</NuxtLink></li>
                                    <li><NuxtLink to="/blog">Blog</NuxtLink></li>
                                    <li><NuxtLink to="/service">Services</NuxtLink></li>
                                    <li><NuxtLink to="/contact">Contact</NuxtLink></li>
                                </ul>
                            </nav>
                            <button class="vs-menu-toggle d-inline-block d-lg-none"><i class="fal fa-bars"></i></button>
                        </div>
                        <div class="col-auto  d-none d-lg-block">
                            <div class="header-icons">
                                <button class="simple-icon sideMenuToggler"><i class="far fa-bars"></i></button>
                            </div>
                        </div>
                        <div class="col-auto d-none d-xl-block">
                            <NuxtLink to="/contact" class="vs-btn sideMenuToggler">Apply Today</NuxtLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>
