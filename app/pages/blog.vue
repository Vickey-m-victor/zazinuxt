<template>
    <div>
        <AppBreadcrumb title="Our Blogs" />
        <section class="vs-blog-wrapper space-top space-extra-bottom">
            <div class="container">
                <div class="row gx-40">
                    <BlogList />
                    <BlogSidebar />
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
useHead({
    title: 'Our Blogs - Kiddino'
})
</script>
