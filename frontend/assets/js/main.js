import 'jquery'
import 'slick-carousel'


import './responsivemultimenu.js'
import './scripts.js'

require.context('../html/', true);
require.context('../js/', true, /\.(html)/);
require.context('../images', true);
require('../scss/main.scss');


