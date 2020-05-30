from flask_assets import Bundle


def compile_assets(assets):

    js = Bundle('vendor/jquery/jquery-3.2.1.min.js',
                'vendor/animsition/js/animsition.min.js',
                'vendor/bootstrap/js/popper.js',
                'vendor/bootstrap/js/bootstrap.min.js',
                'vendor/countdowntime/countdowntime.js',
                'vendor/lightbox2/js/lightbox.min.js',
                'vendor/slick/slick.min.js',
                'js/slick-custom.js',
                'vendor/select2/select2.min.js',
                'js/main.js',
                filters='jsmin',
                output='js/all-min.js')

    css = Bundle('vendor/bootstrap/css/bootstrap.min.css',
                 'fonts/font-awesome-4.7.0/css/font-awesome.min.css',
                 'fonts/themify/themify-icons.css',
                 'fonts/Linearicons-Free-v1.0.0/icon-font.min.css',
                 'fonts/elegant-font/html-css/style.css',
                 'vendor/animate/animate.css',
                 'vendor/animsition/css/animsition.min.css',
                 'vendor/noui/nouislider.min.css',
                 'vendor/select2/select2.min.css',
                 'vendor/daterangepicker/daterangepicker.css',
                 'vendor/slick/slick.css',
                 'vendor/css-hamburgers/hamburgers.min.css',
                 'vendor/lightbox2/css/lightbox.min.css',
                 'css/util.css',
                 'css/main.css',
                 filters='cssmin',
                 output='css/all-min.css')

    assets.register('js_all', js)
    assets.register('css_all', css)
