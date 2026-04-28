<template>
    <div class="breadcumb-wrapper" data-bg-src="/img/breadcumb/breadcumb-bg.jpg">
        <div class="container z-index-common">
            <div class="breadcumb-content">
                <h1 class="breadcumb-title">{{ title }}</h1>
                <p class="breadcumb-text">{{ text }}</p>
                <div class="breadcumb-menu-wrap">
                    <ul class="breadcumb-menu">
                        <li><NuxtLink href="/">Home</NuxtLink></li>
                        <li>{{ title }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true
    },
    text: {
        type: String,
        default: 'Montessori Is A Nurturing And Holistic Approach To Learning'
    }
})
</script>
