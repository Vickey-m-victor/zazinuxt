// ~/plugins/legacy-js.client.ts
export default defineNuxtPlugin(() => {
  const scriptPaths = [
    '/js/vendor/jquery-3.6.0.min.js',
    '/js/bootstrap.min.js',
    '/js/datecounter.js',
    '/js/imagesloaded.pkgd.min.js',
    '/js/isotope.pkgd.min.js',
    '/js/jquery.counterup.min.js',
    '/js/jquery-ui.min.js',
    '/js/jquery.fancybox.js',
    '/js/jquery.magnific-popup.min.js',
    '/js/jquery.waypoints.min.js',
    '/js/layerslider.kreaturamedia.jquery.js',
    '/js/layerslider.transitions.js',
    '/js/layerslider.utils.js',
    '/js/slick.min.js',
    '/js/main.js'
  ]

  scriptPaths.forEach((path) => {
    const script = document.createElement('script')
    script.src = path
    script.async = false // ensures scripts execute in the order they are appended
    script.defer = true
    document.head.appendChild(script)
  })
})
