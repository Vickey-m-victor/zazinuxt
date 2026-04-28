<template>
    <div class="col-lg-4">
        <aside class="sidebar-area">
            <div class="widget widget_search   ">
                <h3 class="widget_title">Search</h3>
                <form class="search-form">
                    <input type="text" placeholder="Search Here">
                    <button type="submit"><i class="far fa-search"></i></button>
                </form>
            </div>
            <div class="widget  ">
                <h3 class="widget_title">Latest News</h3>
                <div class="recent-post-wrap">
                    <div class="recent-post">
                        <div class="media-img">
                            <NuxtLink to="/blog-details"><img src="/img/blog/recent-post-1-1.jpg" alt="Blog Image"></NuxtLink>
                        </div>
                        <div class="media-body">
                            <div class="recent-post-meta">
                                <NuxtLink to="/blog"><i class="far fa-calendar-alt"></i>December 3, 2022</NuxtLink>
                            </div>
                            <h4 class="post-title"><NuxtLink class="text-inherit" to="/blog-details">A very warm welcome
                                    to our new Treasurer</NuxtLink></h4>
                        </div>
                    </div>
                    <div class="recent-post">
                        <div class="media-img">
                            <NuxtLink to="/blog-details"><img src="/img/blog/recent-post-1-2.jpg" alt="Blog Image"></NuxtLink>
                        </div>
                        <div class="media-body">
                            <div class="recent-post-meta">
                                <NuxtLink to="/blog"><i class="far fa-calendar-alt"></i>February 15, 2022</NuxtLink>
                            </div>
                            <h4 class="post-title"><NuxtLink class="text-inherit" to="/blog-details">German kinder and
                                    garten mean child</NuxtLink></h4>
                        </div>
                    </div>
                    <div class="recent-post">
                        <div class="media-img">
                            <NuxtLink to="/blog-details"><img src="/img/blog/recent-post-1-3.jpg" alt="Blog Image"></NuxtLink>
                        </div>
                        <div class="media-body">
                            <div class="recent-post-meta">
                                <NuxtLink to="/blog"><i class="far fa-calendar-alt"></i>Augest 20, 2022</NuxtLink>
                            </div>
                            <h4 class="post-title"><NuxtLink class="text-inherit" to="/blog-details">English uses term to
                                    refer to the earliest</NuxtLink></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div class="widget widget_categories   ">
                <h3 class="widget_title">Categories</h3>
                <ul>
                    <li>
                        <NuxtLink to="/blog">TODDLER</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/blog">PRESCHOOL</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/blog">KINDERGARTEN</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/blog">PRE-K PROGRAM</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/blog">AFTER SCHOOL</NuxtLink>
                    </li>
                </ul>
            </div>
            <div class="widget  ">
                <h4 class="widget_title">Photos Gallery</h4>
                <div class="sidebar-gallery">
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-1.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-1.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-2.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-2.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-3.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-3.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-4.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-4.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-5.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-5.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                    <div class="gallery-thumb">
                        <img src="/img/widget/gal-1-6.jpg" alt="Gallery Image" class="w-100">
                        <NuxtLink href="/img/widget/gal-1-6.jpg" class="popup-image gal-btn"><i class="fal fa-plus"></i></NuxtLink>
                    </div>
                </div>
            </div>
            <div class="widget  ">
                <h3 class="widget_title">Video</h3>
                <div class="vs-video-widget">
                    <div class="video-thumb mega-hover">
                        <img src="/img/blog/intro-video-thumb.jpg" alt="Video Thumb" class="w-100">
                        <NuxtLink href="https://www.youtube.com/watch?v=_sI_Ps7JSEk"
                            class="play-btn popup-video position-center"><i class="fas fa-play"></i></NuxtLink>
                    </div>
                    <h4 class="video-title h5"><NuxtLink href="https://www.youtube.com/watch?v=_sI_Ps7JSEk"
                            class="text-inherit popup-video">A very warm welcome to our new Treasurer</NuxtLink>
                    </h4>
                </div>
            </div>
            <div class="widget widget_tag_cloud   ">
                <h3 class="widget_title">Upcoming Events</h3>
                <div class="vs-event-widget">
                    <div class="recent-event">
                        <NuxtLink to="/event-details" class="event-date"><span class="month">Dec</span>24</NuxtLink>
                        <div class="media-body">
                            <h4 class="event-title"><NuxtLink to="/event-details" class="text-inherit">Father`s Day
                                    Sundaes & Shaving!</NuxtLink></h4>
                        </div>
                    </div>
                    <div class="recent-event">
                        <NuxtLink to="/event-details" class="event-date"><span class="month">Dec</span>24</NuxtLink>
                        <div class="media-body">
                            <h4 class="event-title"><NuxtLink to="/event-details" class="text-inherit">Father`s Day
                                    Sundaes & Shaving!</NuxtLink></h4>
                        </div>
                    </div>
                    <div class="recent-event">
                        <NuxtLink to="/event-details" class="event-date"><span class="month">Dec</span>24</NuxtLink>
                        <div class="media-body">
                            <h4 class="event-title"><NuxtLink to="/event-details" class="text-inherit">Father`s Day
                                    Sundaes & Shaving!</NuxtLink></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div class="widget bg-vs-secondary  " data-bg-src="/img/bg/widget-bg-1-1.png">
                <h4 class="mt-n2 text-white">Join together to make amazing things happen</h4>
                <p class="mb-4 pb-1 text-white">Get all the latest information, support and guidance about
                    the cost of living with kindergarten.</p>
                <NuxtLink to="/registration" class="vs-btn">Start Registration</NuxtLink>
            </div>
        </aside>
    </div>
</template>
