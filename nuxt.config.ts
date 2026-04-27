// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  app: {
    head: {
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Jost:wght@400;500&display=swap' }
      ]
    }
  },
  css: [
    '~/assets/css/bootstrap.min.css',
    '~/assets/css/fontawesome.min.css',
    '~/assets/css/layerslider.min.css',
    '~/assets/css/magnific-popup.min.css',
    '~/assets/css/slick.min.css',
    '~/assets/css/style.css'
  ],
  plugins: [
    '~/plugins/legacy-js.client'
  ]
})