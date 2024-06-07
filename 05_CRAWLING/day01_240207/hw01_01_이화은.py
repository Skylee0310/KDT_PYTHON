from urllib.request import urlopen
from bs4 import BeautifulSoup

html_example = '''
<html class=" js flexbox flexboxlegacy canvas canvastext webgl no-touch geolocation postmessage no-websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers no-applicationcache svg inlinesvg smil svgclippaths" style=""><head>
        <!-- Meta -->
        <meta name="viewport" content="width=device-width">
        <link rel="schema.DC" href="http://purl.org/dc/elements/1.1/"><title>7-Day Forecast 37.77N 122.41W</title><meta name="DC.title" content="National Weather Service"><meta name="DC.description" content="NOAA National Weather Service National Weather Service"><meta name="DC.creator" content="US Department of Commerce, NOAA, National Weather Service"><meta name="DC.date.created" scheme="ISO8601" content=""><meta name="DC.language" scheme="DCTERMS.RFC1766" content="EN-US"><meta name="DC.keywords" content="weather, National Weather Service"><meta name="DC.publisher" content="NOAA's National Weather Service"><meta name="DC.contributor" content="National Weather Service"><meta name="DC.rights" content="//www.weather.gov/disclaimer.php"><meta name="rating" content="General"><meta name="robots" content="index,follow">

        <!-- Icons -->
        <link rel="shortcut icon" href="./images/favicon.ico" type="image/x-icon">

        <!-- CSS -->
        <link rel="stylesheet" href="css/bootstrap-3.2.0.min.css">
        <link rel="stylesheet" href="css/bootstrap-theme-3.2.0.min.css">
        <link rel="stylesheet" href="css/font-awesome-4.3.0.min.css">
        <link rel="stylesheet" href="css/ol-4.6.4.css" type="text/css">
        <link rel="stylesheet" type="text/css" href="css/mapclick.css">
        <!--[if lte IE 7]><link rel="stylesheet" type="text/css" href="css/bootstrap-ie7.css" /><![endif]-->
        <!--[if lte IE 9]><link rel="stylesheet" type="text/css" href="css/mapclick-ie.css" /><![endif]-->
        <link rel="stylesheet" type="text/css" href="css/print.css">
        <link rel="stylesheet" type="text/css" href="css/search.css">

        <!-- Javascript -->
        <script type="text/javascript" async="" src="https://www.google-analytics.com/plugins/ua/linkid.js"></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="//cdnmon.cfigroup.com/source/webmon/ce989efe8b1040/webmon.js"></script><script type="text/javascript" src="js/lib/modernizr-2.8.3.js"></script>
        <script type="text/javascript" src="js/lib/json3-3.3.2.min.js"></script>
        <script type="text/javascript" src="js/lib/jquery-1.11.3.min.js"></script>
        <script type="text/javascript" src="js/lib/jquery.hoverIntent-1.8.1.min.js"></script>
        <script type="text/javascript" src="js/lib/bootstrap-3.2.0.min.js"></script>
        <script type="text/javascript" src="js/lib/ol-4.6.4.js"></script>
        <!--[if lte IE 8]><script type="text/javascript" src="js/respond.min.js"></script><![endif]-->
        <script type="text/javascript" src="js/jquery.autocomplete.min.js"></script>
        <script type="text/javascript" src="js/cfisurvey/cfi.js?v2"></script>
        <script type="text/javascript" src="js/forecast.esri.js"></script>
        <script type="text/javascript" src="js/forecast.search.js"></script>
        <script type="text/javascript" src="js/forecast.openlayers.js"></script>
        <script type="text/javascript" src="js/browserSniffer.js"></script>
        <script type="text/javascript" id="_fed_an_ua_tag" src="https://dap.digitalgov.gov/Universal-Federated-Analytics-Min.js?agency=DOC&amp;subagency=NOAA"></script><script type="text/javascript" src="https://www.googletagmanager.com/gtag/js?id=G-CSLL4ZEK4L"></script>
        <script type="text/javascript">
            // GoogleAnalyticsObject is defined in the federated analytics script, but PUA option not used as forecast UA needs sampleRate
            window[window['GoogleAnalyticsObject']]('create', 'UA-40768555-1', 'weather.gov', {'sampleRate': 6});
            window[window['GoogleAnalyticsObject']]('set', 'anonymizeIp', true);
            window[window['GoogleAnalyticsObject']]('require', 'linkid');
            window[window['GoogleAnalyticsObject']]('send', 'pageview');
        </script>
        <script type="javascript">
// ForeSee Staging Embed Script v2.01
// DO NOT MODIFY BELOW THIS LINE *****************************************
;(function (g) {
  var d = document, am = d.createElement('script'), h = d.head || d.getElementsByTagName("head")[0], fsr = 'fsReady',
  aex = { 
    "src": "//gateway.foresee.com/sites/weather-gov/production/gateway.min.js",
    "type": "text/javascript", 
    "async": "true", 
    "data-vendor": "fs", 
    "data-role": "gateway" 
  };
  for (var attr in aex) { am.setAttribute(attr, aex[attr]); } h.appendChild(am); g[fsr] || (g[fsr] = function () { var aT = '__' + fsr + '_stk__'; g[aT] = g[aT] || []; g[aT].push(arguments); });
})(window);
// DO NOT MODIFY ABOVE THIS LINE *****************************************
</script>
    </head>
    <body>
        <main class="container">
                    <header class="row clearfix" id="page-header">
            <a href="//www.noaa.gov" id="header-noaa" class="pull-left"><img src="/css/images/header_noaa.png" alt="National Oceanic and Atmospheric Administration"></a>
            <a href="//www.weather.gov" id="header-nws" class="pull-left"><img src="/css/images/header_nws.png" alt="National Weather Service"></a>
            <a href="//www.commerce.gov" id="header-doc" class="pull-right"><img src="/css/images/header_doc.png" alt="United States Department of Commerce"></a>
        </header>
        
                    <nav class="navbar navbar-default row" role="navigation">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#top-nav">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
                <div class="collapse navbar-collapse" id="top-nav">
                    <ul class="nav navbar-nav">
                        <li><a href="//www.weather.gov">HOME</a></li>
                        <li class="dropdown"><a href="http://www.weather.gov/forecastmaps" class="dropdown-toggle" data-toggle="dropdown">FORECAST&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="http://www.weather.gov">Local</a></li><li><a href="http://digital.weather.gov">Graphical</a></li><li><a href="http://www.aviationweather.gov/">Aviation</a></li><li><a href="http://www.weather.gov/marine">Marine</a></li><li><a href="http://water.weather.gov/ahps/">Rivers and Lakes</a></li><li><a href="http://www.nhc.noaa.gov/">Hurricanes</a></li><li><a href="http://www.spc.noaa.gov/">Severe Weather</a></li><li><a href="http://www.weather.gov/fire/">Fire Weather</a></li><li><a href="https://www.esrl.noaa.gov/gmd/grad/solcalc/sunrise.html">Sun/Moon</a></li><li><a href="http://www.cpc.ncep.noaa.gov/">Long Range Forecasts</a></li><li><a href="http://www.cpc.ncep.noaa.gov">Climate Prediction</a></li><li><a href="https://www.swpc.noaa.gov/">Space Weather</a></li></ul>                            </li>
                            <li class="dropdown"><a href="https://www.weather.gov/wrh/climate/" class="dropdown-toggle" data-toggle="dropdown">PAST WEATHER&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="https://www.weather.gov/wrh/climate/">Past Weather</a></li><li><a href="https://www.weather.gov/wrh/climate/">Heating/Cooling Days</a></li><li><a href="https://www.weather.gov/wrh/climate/">Monthly Temperatures</a></li><li><a href="https://www.weather.gov/wrh/climate/">Records</a></li><li><a href="http://aa.usno.navy.mil/">Astronomical Data</a></li></ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/safety" class="dropdown-toggle" data-toggle="dropdown">SAFETY&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="https://www.weather.gov/safety/tsunami">Tsunamis</a></li><li><a href="https://www.weather.gov/safety/flood">Floods</a></li><li><a href="https://www.weather.gov/safety/beachhazards">Beach Hazards</a></li><li><a href="https://www.weather.gov/safety/wildfire">Wildfire</a></li><li><a href="https://www.weather.gov/safety/cold">Cold</a></li><li><a href="https://www.weather.gov/safety/tornado">Tornadoes</a></li><li><a href="https://www.weather.gov/safety/airquality">Air Quality</a></li><li><a href="https://www.weather.gov/safety/fog">Fog</a></li><li><a href="https://www.weather.gov/safety/heat">Heat</a></li><li><a href="https://www.weather.gov/safety/hurricane">Hurricanes</a></li><li><a href="https://www.weather.gov/safety/lightning">Lightning</a></li><li><a href="https://www.weather.gov/safety/safeboating">Safe Boating</a></li><li><a href="https://www.weather.gov/safety/ripcurrent">Rip Currents</a></li><li><a href="https://www.weather.gov/safety/thunderstorm">Thunderstorms</a></li><li><a href="https://www.weather.gov/safety/space">Space Weather</a></li><li><a href="https://www.weather.gov/safety/heat-uv">Sun (Ultraviolet Radiation)</a></li><li><a href="http://www.weather.gov/safetycampaign">Safety Campaigns</a></li><li><a href="https://www.weather.gov/safety/wind">Wind</a></li><li><a href="https://www.weather.gov/safety/drought">Drought</a></li><li><a href="https://www.weather.gov/safety/winter">Winter Weather</a></li></ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/informationcenter" class="dropdown-toggle" data-toggle="dropdown">INFORMATION&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="http://www.weather.gov/wrn/wea">Wireless Emergency Alerts</a></li><li><a href="https://www.weather.gov/owlie/publication_brochures">Brochures</a></li><li><a href="http://www.weather.gov/wrn/">Weather-Ready Nation</a></li><li><a href="https://www.weather.gov/coop/">Cooperative Observers</a></li><li><a href="http://www.weather.gov/briefing/">Daily Briefing</a></li><li><a href="http://www.nws.noaa.gov/om/hazstats.shtml">Damage/Fatality/Injury Statistics</a></li><li><a href="http://mag.ncep.noaa.gov/">Forecast Models</a></li><li><a href="https://www.weather.gov/gis">GIS Data Portal</a></li><li><a href="https://www.weather.gov/nwr/">NOAA Weather Radio</a></li><li><a href="http://weather.gov/publications">Publications</a></li><li><a href="http://www.weather.gov/SKYWARN">SKYWARN Storm Spotters</a></li><li><a href="http://www.weather.gov/StormReady">StormReady</a></li><li><a href="https://www.weather.gov/TsunamiReady/">TsunamiReady</a></li><li><a href="https://www.weather.gov/notification/">Service Change Notices</a></li></ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/education" class="dropdown-toggle" data-toggle="dropdown">EDUCATION&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="https://www.weather.gov/wrn/force">Be A Force of Nature</a></li><li><a href="http://www.weather.gov/owlie">NWS Education Home</a></li></ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/news/" class="dropdown-toggle" data-toggle="dropdown">NEWS&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="http://www.weather.gov/news">NWS News</a></li><li><a href="https://www.weather.gov/wrn/calendar">Events</a></li><li><a href="https://www.weather.gov/owlie/publication_brochures">Pubs/Brochures/Booklets </a></li><li><a href="http://www.noaa.gov/NOAA-Communications">NWS Media Contacts</a></li></ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/search" class="dropdown-toggle" data-toggle="dropdown">SEARCH&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu">                                <li><!-- Begin search code -->
                                    <div id="site-search">
                                        <form method="get" action="//search.usa.gov/search" style="margin-bottom: 0; margin-top: 0;">
                                            <input type="hidden" name="v:project" value="firstgov">
                                            <label for="query">Search For</label>
                                            <input type="text" name="query" id="query" size="12">
                                            <input type="submit" value="Go">
                                            <p>
                                                <input type="radio" name="affiliate" checked="checked" value="nws.noaa.gov" id="nws">
                                                <label for="nws" class="search-scope">NWS</label>
                                                <input type="radio" name="affiliate" value="noaa.gov" id="noaa">
                                                <label for="noaa" class="search-scope">All NOAA</label>
                                            </p>
                                        </form>
                                    </div>
                                </li>
                                </ul>                            </li>
                            <li class="dropdown"><a href="http://www.weather.gov/about" class="dropdown-toggle" data-toggle="dropdown">ABOUT&nbsp;<span class="caret"></span></a><ul class="dropdown-menu" role="menu"><li><a href="http://www.weather.gov/about">About NWS</a></li><li><a href="http://www.weather.gov/organization">Organization</a></li><li><a href="https://www.weather.gov/media/wrn/NWS-2023-Strategic-Plan.pdf">Strategic Plan</a></li><li><a href="http://www.weather.gov/careers/#diversity">Commitment to Diversity</a></li><li><a href="https://sites.google.com/a/noaa.gov/nws-insider/">For NWS Employees</a></li><li><a href="http://www.weather.gov/insider">International</a></li><li><a href="http://www.weather.gov/ncep">National Centers</a></li><li><a href="http://www.weather.gov/careers/">Careers</a></li><li><a href="http://www.weather.gov/contact">Contact Us</a></li><li><a href="https://w1.weather.gov/glossary">Glossary</a></li><li><a href="https://weather.gov/socialmedia">Social Media</a></li></ul>                            </li>
                                                </ul>
                </div>
            </div>
        </nav>
        
        <div class="contentArea">
            <!-- Start Forecastsearch -->
    <div class="" id="fcst-search">
        <form name="getForecast" id="getForecast" class="form-inline" role="form" action="https://forecast.weather.gov/zipcity.php" method="get">
        <div id="getfcst-body">
            <input name="inputstring" type="text" class="form-control" id="inputstring" placeholder="" autocomplete="off">
            <input name="btnSearch" id="btnSearch" class="btn btn-default" type="submit" value="Go">
            <div id="txtHelp"><a href="javascript:void(window.open('http://weather.gov/ForecastSearchHelp.html','locsearchhelp','status=0,toolbar=0,location=0,menubar=0,directories=0,resizable=1,scrollbars=1,height=500,width=530').focus());">View Location Examples</a></div>
        </div>
        <div id="txtError">
            <div id="errorNoResults" style="display:none;">Sorry, the location you searched for was not found. Please try another search.</div>
            <div id="errorMultipleResults" style="display:none">Multiple locations were found. Please select one of the following:</div>
            <div id="errorChoices" style="display:none"></div>
            <input id="btnCloseError" type="button" value="Close" style="display:none">
        </div>
        <div id="getfcst-head">
            <p>Your local forecast office is</p>
            <h3 id="getfcst-headOffice"><a href="https://www.weather.gov/mtr">San Francisco Bay Area/Monterey, CA</a></h3>
        </div>
        </form>
    </div>
    <!-- end Forecastsearch -->
        
        <link rel="stylesheet" type="text/css" href="/css/topnews.css">
<div id="news-items">
    <div id="topnews">
    <div class="icon"><img src="/images/news-important.jpg"></div>
    <div class="body">
        <h1 style="font-size: 11pt;">Heavy Rain and Flooding Threat Across the Southwest; Heavy Snow in the Intermountain West; Flooding Threat in Puerto Rico and the U.S Virgin Islands</h1>
        <p>
            A storm system will push into the Southwest, bringing heavy rain and a flooding threat today. Heavy snow will spread into the Intermountain West and Rockies. High snowfall rates and strong winds could lead to difficult travel conditions. A wet pattern will continue heavy rain and the threat for flash flooding across Puerto Rico and the U.S Virgin Islands through Thursday.
            <a href="http://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=pmdspd" target="_blank">Read More &gt;</a>
        </p>
    </div>
</div>

</div>
        <script type="text/javascript">(function ($) { var topnews = $("#topnews"); topnews.hide(); $.get("siteNews.php", {a:"mtr"},function(response){ if (response !== "false") topnews.replaceWith($(response)); topnews.show(); }); })(jQuery);</script><!-- PageFormat-Land -->
<script language="javascript">document.title = '7-Day Forecast 37.77N 122.41W';</script><img src="images/track_land_point.png" style="display:none;"><div class="panel panel-danger"><div class="panel-heading"><h3 class="panel-title">Hazardous Weather Conditions</h3></div><div class="panel-body"><ul><li><a id="hazard-CAZ006-Coastal+Flood+Advisory-0" href="showsigwx.php?warnzone=CAZ006&amp;warncounty=CAC075&amp;firewxzone=CAZ006&amp;local_place1=San Francisco CA&amp;product1=Coastal+Flood+Advisory&amp;lat=37.7772&amp;lon=-122.4168" class="anchor-hazards">Coastal Flood Advisory  until February 10, 10:00 AM PST</a></li><li><a id="hazard-CAZ006-Beach+Hazards+Statement-1" href="showsigwx.php?warnzone=CAZ006&amp;warncounty=CAC075&amp;firewxzone=CAZ006&amp;local_place1=San Francisco CA&amp;product1=Beach+Hazards+Statement&amp;lat=37.7772&amp;lon=-122.4168" class="anchor-hazards">Beach Hazards Statement  until February 7, 04:00 AM PST</a></li></ul></div></div>
<div id="quickLinks">
    <span class="lang-spanish"><a href="//forecast.weather.gov/MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;lg=sp">En Español</a></span>
</div>

<!-- Current Conditions -->
<div id="current-conditions" class="panel panel-default">

    <!-- Current Conditions header row -->
    <div class="panel-heading">
        <div>
            <b>Current conditions at</b>
            <h2 class="panel-title">SAN FRANCISCO DOWNTOWN (SFOC1)</h2>
            <span class="smallTxt"><b>Lat:&nbsp;</b>37.77056°N<b>Lon:&nbsp;</b>122.42694°W<b>Elev:&nbsp;</b>150.0ft.</span>
        </div>
    </div>
    <div class="panel-body" id="current-conditions-body">
        <!-- Graphic and temperatures -->
        <div id="current_conditions-summary" class="pull-left">
                        <p class="myforecast-current">NA</p>
            <p class="myforecast-current-lrg">50°F</p>
            <p class="myforecast-current-sm">10°C</p>
        </div>
        <div id="current_conditions_detail" class="pull-left">
            <table>
            <tbody><tr>
            <td class="text-right"><b>Humidity</b></td>
            <td>77%</td>
            </tr>
            <tr>
            <td class="text-right"><b>Wind Speed</b></td>
            <td>NA NA MPH</td>
            </tr>
            <tr>
            <td class="text-right"><b>Barometer</b></td>
            <td>NA</td>
            </tr>
            <tr>
            <td class="text-right"><b>Dewpoint</b></td>
            <td>43°F (6°C)</td>
            </tr>
            <tr>
            <td class="text-right"><b>Visibility</b></td>
            <td>NA</td>
            </tr>
                        <tr>
            <td class="text-right"><b>Last update</b></td>
            <td>
                06 Feb 09:43 PM PST            </td>
            </tr>
            </tbody></table>
        </div>
        <div id="current_conditions_station">
            <div class="current-conditions-extra">
                            <!-- Right hand section -->
            <p class="moreInfo"><b>More Information:</b></p><p><a id="localWFO" href="https://www.weather.gov/mtr" title="San Francisco Bay Area/Monterey, CA"><span class="hideText">Local</span> Forecast Office</a><a id="moreWx" href="https://www.weather.gov/wrh/LocalWeather?zone=CAZ006">More Local Wx</a><a href="https://www.wrh.noaa.gov/mesowest/getobext.php?wfo=mtr&amp;sid=SFOC1&amp;num=72&amp;raw=0">3 Day History</a><a id="mobileWxLink" href="//mobile.weather.gov/index.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english">Mobile Weather</a><a id="wxGraph" href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=graphical">Hourly <span class="hideText">Weather </span>Forecast</a></p>            </div>
        <!-- /current_conditions_station -->
        </div>
        <!-- /current-conditions-body -->
    </div>
<!-- /Current Conditions -->
</div>

<!-- 7-Day Forecast -->
<div id="seven-day-forecast" class="panel panel-default">
    <div class="panel-heading">
    <b>Extended Forecast for</b>
    <h2 class="panel-title">
                San Francisco CA    </h2>
    </div>
    <div class="panel-body" id="seven-day-forecast-body">
            <div id="seven-day-forecast-container"><div id="headline-container" class="current-hazard" style="margin-left: 124px"><div id="headline-separator" style="top: 34px; height: 131px"></div><div id="headline-info" style="margin-top: 5px" onclick="$('#headline-detail').toggle(); $('#headline-detail-now').hide()"><div id="headline-detail"><div>Coastal Flood Advisory until February 10, 10:00am</div></div><span class="fa fa-info-circle"></span>Click here for hazard details and duration</div><div class="headline-bar headline-advisory " style="top: 40px; left: 19px; height: 125px; width: 890px">
<div class="headline-title">Coastal Flood Advisory</div>
</div></div><ul id="seven-day-forecast-list" class="list-unstyled" style="padding-top: 60px"><li class="forecast-tombstone current-hazard current-hazard-advisory" onclick="$('#headline-detail-now').toggle(); $('#headline-detail').hide()">
<div class="top-bar">&nbsp;<div id="headline-detail-now"><div>Coastal Flood Advisory until February 10, 10:00am</div></div><span class="tab"></span><span class="fa fa-info-circle"></span></div><div class="tombstone-container">
<p class="period-name">NOW until<br>10:00am Sat</p>
<p><img src="DualImage.php?i=nskc&amp;j=nra&amp;jp=80" alt="" title="" class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Coastal Flood Advisory</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tonight<br><br></p>
<p><img src="DualImage.php?i=nskc&amp;j=nra&amp;jp=80" alt="Tonight: Rain after 4am.  Low around 47. West northwest wind around 11 mph.  Chance of precipitation is 80%." title="Tonight: Rain after 4am.  Low around 47. West northwest wind around 11 mph.  Chance of precipitation is 80%." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Clear then<br>Rain</p><p class="temp temp-low">Low: 47 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br><br></p>
<p><img src="newimages/medium/ra80.png" alt="Wednesday: Rain, mainly before 4pm.  High near 54. West wind 9 to 18 mph becoming south southwest in the morning. Winds could gust as high as 22 mph.  Chance of precipitation is 80%. New precipitation amounts between a tenth and quarter of an inch possible. " title="Wednesday: Rain, mainly before 4pm.  High near 54. West wind 9 to 18 mph becoming south southwest in the morning. Winds could gust as high as 22 mph.  Chance of precipitation is 80%. New precipitation amounts between a tenth and quarter of an inch possible. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Rain</p><p class="temp temp-high">High: 54 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br>Night</p>
<p><img src="DualImage.php?i=nra&amp;j=nbkn&amp;ip=20" alt="Wednesday Night: A 20 percent chance of rain before 10pm.  Mostly cloudy, with a low around 45. North wind 9 to 14 mph, with gusts as high as 18 mph.  New precipitation amounts of less than a tenth of an inch possible. " title="Wednesday Night: A 20 percent chance of rain before 10pm.  Mostly cloudy, with a low around 45. North wind 9 to 14 mph, with gusts as high as 18 mph.  New precipitation amounts of less than a tenth of an inch possible. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Slight Chance<br>Rain then<br>Mostly Cloudy</p><p class="temp temp-low">Low: 45 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br><br></p>
<p><img src="newimages/medium/bkn.png" alt="Thursday: Partly sunny, with a high near 56. North wind 5 to 15 mph becoming west northwest in the afternoon. Winds could gust as high as 20 mph. " title="Thursday: Partly sunny, with a high near 56. North wind 5 to 15 mph becoming west northwest in the afternoon. Winds could gust as high as 20 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Partly Sunny</p><p class="temp temp-high">High: 56 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br>Night</p>
<p><img src="newimages/medium/nsct.png" alt="Thursday Night: Partly cloudy, with a low around 44. North wind 5 to 9 mph. " title="Thursday Night: Partly cloudy, with a low around 44. North wind 5 to 9 mph. " class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Partly Cloudy</p><p class="temp temp-low">Low: 44 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Friday<br><br></p>
<p><img src="newimages/medium/sct.png" alt="Friday: Mostly sunny, with a high near 56." title="Friday: Mostly sunny, with a high near 56." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Mostly Sunny</p><p class="temp temp-high">High: 56 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Friday<br>Night</p>
<p><img src="newimages/medium/nsct.png" alt="Friday Night: Partly cloudy, with a low around 44." title="Friday Night: Partly cloudy, with a low around 44." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Partly Cloudy</p><p class="temp temp-low">Low: 44 °F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Saturday<br><br></p>
<p><img src="newimages/medium/few.png" alt="Saturday: Sunny, with a high near 59." title="Saturday: Sunny, with a high near 59." class="forecast-icon"></p><p class="short-desc" style="height: 54px;">Sunny</p><p class="temp temp-high">High: 59 °F</p></div></li></ul></div>
<script type="text/javascript">
// equalize forecast heights
$(function () {
    var maxh = 0;
    $(".forecast-tombstone .short-desc").each(function () {
        var h = $(this).height();
        if (h > maxh) { maxh = h; }
    });
    $(".forecast-tombstone .short-desc").height(maxh);
});
</script>    </div>
</div>

<!-- Everything between 7-Day Forecast and Footer goes in this row -->
<div id="floatingDivs" class="row">
    <!-- Everything on the left-hand side -->
    <div class="col-md-7 col-lg-8">
        <!-- Detailed Forecast -->
        <div id="detailed-forecast" class="panel panel-default">
        <div class="panel-heading">
            <h2 class="panel-title">Detailed Forecast</h2>
        </div>
        <div class="panel-body" id="detailed-forecast-body">
            <div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Tonight</b></div><div class="col-sm-10 forecast-text">Rain after 4am.  Low around 47. West northwest wind around 11 mph.  Chance of precipitation is 80%.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Wednesday</b></div><div class="col-sm-10 forecast-text">Rain, mainly before 4pm.  High near 54. West wind 9 to 18 mph becoming south southwest in the morning. Winds could gust as high as 22 mph.  Chance of precipitation is 80%. New precipitation amounts between a tenth and quarter of an inch possible. </div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Wednesday Night</b></div><div class="col-sm-10 forecast-text">A 20 percent chance of rain before 10pm.  Mostly cloudy, with a low around 45. North wind 9 to 14 mph, with gusts as high as 18 mph.  New precipitation amounts of less than a tenth of an inch possible. </div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Thursday</b></div><div class="col-sm-10 forecast-text">Partly sunny, with a high near 56. North wind 5 to 15 mph becoming west northwest in the afternoon. Winds could gust as high as 20 mph. </div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Thursday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 44. North wind 5 to 9 mph. </div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Friday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 56.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Friday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 44.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Saturday</b></div><div class="col-sm-10 forecast-text">Sunny, with a high near 59.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Saturday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 46.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Sunday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 59.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Sunday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 46.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Monday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 60.</div></div><div class="row row-odd row-forecast"><div class="col-sm-2 forecast-label"><b>Monday Night</b></div><div class="col-sm-10 forecast-text">Partly cloudy, with a low around 47.</div></div><div class="row row-even row-forecast"><div class="col-sm-2 forecast-label"><b>Tuesday</b></div><div class="col-sm-10 forecast-text">Mostly sunny, with a high near 61.</div></div>        </div>
    </div>
    <!-- /Detailed Forecast -->

        
        <!-- Additional Forecasts and Information -->
        <div id="additional_forecasts" class="panel panel-default">
        <div class="panel-heading">
        <h2 class="panel-title">Additional Forecasts and Information</h2>
        </div>

        <div class="panel-body" id="additional-forecasts-body">
        <p class="myforecast-location"><a href="MapClick.php?zoneid=CAZ006">Zone Area Forecast for San Francisco County, CA</a></p>
                <!-- First nine-ten links -->
        <div id="linkBlockContainer">
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="//forecast.weather.gov/product.php?site=MTR&amp;issuedby=MTR&amp;product=AFD&amp;format=CI&amp;version=1&amp;glossary=1">Forecast Discussion</a></li>
                    <li><a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=text&amp;TextType=2">Printable Forecast</a></li>
                    <li><a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=text&amp;TextType=1">Text Only Forecast</a></li>
                </ul>
            </div>
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=graphical">Hourly Weather Forecast</a></li>
                    <li><a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=digital">Tabular Forecast</a></li>
                    <!-- <li><a href="afm/PointClick.php?lat=37.7772&lon=-122.4168">Quick Forecast</a></li> -->
                </ul>
            </div>
            <div class="linkBlock">
                <ul class="list-unstyled">
                    <li><a href="//weather.gov/aq/probe_aq_data.php?latitude=37.7772&amp;longitude=-122.4168">Air Quality Forecasts</a></li>
                    <li><a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;FcstType=text&amp;unit=1&amp;lg=en">International System of Units</a></li>
                                        <li><a href="//www.wrh.noaa.gov/forecast/wxtables/index.php?lat=37.7772&amp;lon=-122.4168">Forecast Weather Table Interface</a></li>
                                    </ul>
            </div>
            <!-- /First nine-ten links -->
                <!-- Additional links -->
                    <div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.wrh.noaa.gov/mtr/versprod.php?pil=RR8&amp;sid=RSA" target="_self">Hourly River Stages</a></li><li><a href="http://www.wrh.noaa.gov/mtr/versprod.php?pil=RR5&amp;sid=RSA" target="_self">Hourly Rainfall</a></li></ul></div><div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.wrh.noaa.gov/mtr/wxlinks.php" target="_self">NWS Office Map</a></li><li><a href="http://www.wrh.noaa.gov/mtr/wx_calculator.php" target="_self">Weather Calculator</a></li></ul></div><div class="linkBlock"><ul class="list-unstyled"><li><a href="http://www.nws.noaa.gov/wtf/udaf/area/?site=mtr" target="_self">User Defined Area</a></li></ul></div>
        </div> <!-- /linkBlockContainer -->
        </div><!-- /additional-forecasts-body-->
    </div> <!-- /additional_forecasts -->
    </div> <!-- /Everything on the left-hand side -->

    <!-- right-side-data -->
    <div class="col-md-5 col-lg-4" id="right-side-data">
    <div id="mapAndDescriptionArea">
        <!-- openlayer map -->
            <style>
#custom-search{
display: block;
position: relative;
z-index: 50;
top: 52px;
left: 60px;
}
#esri-geocoder-search{
display: block;
position: relative;
z-index: 50;
top: 52px;
left: 60px;
}
#emap{
margin-top:15px;
cursor:pointer;
height:370px;
width:100%;
border: 1px solid #ccc;
border-radius: 3px;
}
#switch-basemap-container{
}
#basemap-selection-form ul{
list-style: none;
 margin: 0px;
}
#basemap-selection-form li{
float: left;
}
.disclaimer{
margin-top:350px;
margin-left: 5px;
z-index: 100;
position: absolute;
text-transform: none;
}
.esriAttributionLastItem{
text-transform: none;
}
.esriSimpleSlider div{
height:22px;
line-height:20px;
width:20px;
}
#point-forecast-map-label {
text-align:center;
font-weight:bold;
color:black;
}
@media (max-width: 767px) {
#emap{
margin-top:.5em;
height:270px;
}
.disclaimer{
margin-top:250px;
}
}
</style>
<!-- forecast-map -->
<div class="point-forecast-map">
    <div class="point-forecast-map-header text-center">
        <div id="toolbar">
        <div id="switch-basemap-container">
            <div id="basemap-selection-form" title="Choose a Basemap">
            <div id="basemap-menu">
                <select name="basemap-selected" id="basemap-selected" autocomplete="off" title="Basemap Dropdown Menu">
                <option value="none">Select Basemap</option>
                <option value="topo" selected="">Topographic</option>
                <option value="streets">Streets</option>
                <option value="satellite">Satellite</option>
                <option value="ocean">Ocean</option>
                </select>
            </div>
            </div>
            <div id="point-forecast-map-label">
                    Click Map For Forecast
                </div>
        </div><!-- //#switch-basemap-container -->
        <div style="clear:both;"></div>
        </div><!-- //#toolbar -->
    </div><!-- //.point-forecast-map-header -->

    <div id="emap">
        <noscript><center><br><br><b>Map function requires Javascript and a compatible browser.</b></center></noscript>
        <div class="disclaimer"><a href="http://www.weather.gov/disclaimer#esri">Disclaimer</a></div>
    <div class="ol-viewport" data-view="10" style="position: relative; overflow: hidden; width: 100%; height: 100%; touch-action: none;"><canvas class="ol-unselectable" width="1130" height="553" style="width: 100%; height: 100%; display: block;"></canvas><div class="ol-overlaycontainer"></div><div class="ol-overlaycontainer-stopevent"><div class="ol-zoom ol-unselectable ol-control"><button class="ol-zoom-in" type="button" title="Zoom in">+</button><button class="ol-zoom-out" type="button" title="Zoom out">−</button></div><div class="ol-rotate ol-unselectable ol-control ol-hidden"><button class="ol-rotate-reset" type="button" title="Reset rotation"><span class="ol-compass" style="transform: rotate(0rad);">⇧</span></button></div><div class="ol-attribution ol-unselectable ol-control ol-collapsed"><ul><li style=""><a href="https://openlayers.org/"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAHGAAABxgEXwfpGAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAhNQTFRF////AP//AICAgP//AFVVQECA////K1VVSbbbYL/fJ05idsTYJFtbbcjbJllmZszWWMTOIFhoHlNiZszTa9DdUcHNHlNlV8XRIVdiasrUHlZjIVZjaMnVH1RlIFRkH1RkH1ZlasvYasvXVsPQH1VkacnVa8vWIVZjIFRjVMPQa8rXIVVkXsXRsNveIFVkIFZlIVVj3eDeh6GmbMvXH1ZkIFRka8rWbMvXIFVkIFVjIFVkbMvWH1VjbMvWIFVlbcvWIFVla8vVIFVkbMvWbMvVH1VkbMvWIFVlbcvWIFVkbcvVbMvWjNPbIFVkU8LPwMzNIFVkbczWIFVkbsvWbMvXIFVkRnB8bcvW2+TkW8XRIFVkIlZlJVloJlpoKlxrLl9tMmJwOWd0Omh1RXF8TneCT3iDUHiDU8LPVMLPVcLPVcPQVsPPVsPQV8PQWMTQWsTQW8TQXMXSXsXRX4SNX8bSYMfTYcfTYsfTY8jUZcfSZsnUaIqTacrVasrVa8jTa8rWbI2VbMvWbcvWdJObdcvUdszUd8vVeJaee87Yfc3WgJyjhqGnitDYjaarldPZnrK2oNbborW5o9bbo9fbpLa6q9ndrL3ArtndscDDutzfu8fJwN7gwt7gxc/QyuHhy+HizeHi0NfX0+Pj19zb1+Tj2uXk29/e3uLg3+Lh3+bl4uXj4ufl4+fl5Ofl5ufl5ujm5+jmySDnBAAAAFp0Uk5TAAECAgMEBAYHCA0NDg4UGRogIiMmKSssLzU7PkJJT1JTVFliY2hrdHZ3foSFhYeJjY2QkpugqbG1tre5w8zQ09XY3uXn6+zx8vT09vf4+Pj5+fr6/P39/f3+gz7SsAAAAVVJREFUOMtjYKA7EBDnwCPLrObS1BRiLoJLnte6CQy8FLHLCzs2QUG4FjZ5GbcmBDDjxJBXDWxCBrb8aM4zbkIDzpLYnAcE9VXlJSWlZRU13koIeW57mGx5XjoMZEUqwxWYQaQbSzLSkYGfKFSe0QMsX5WbjgY0YS4MBplemI4BdGBW+DQ11eZiymfqQuXZIjqwyadPNoSZ4L+0FVM6e+oGI6g8a9iKNT3o8kVzNkzRg5lgl7p4wyRUL9Yt2jAxVh6mQCogae6GmflI8p0r13VFWTHBQ0rWPW7ahgWVcPm+9cuLoyy4kCJDzCm6d8PSFoh0zvQNC5OjDJhQopPPJqph1doJBUD5tnkbZiUEqaCnB3bTqLTFG1bPn71kw4b+GFdpLElKIzRxxgYgWNYc5SCENVHKeUaltHdXx0dZ8uBI1hJ2UUDgq82CM2MwKeibqAvSO7MCABq0wXEPiqWEAAAAAElFTkSuQmCC"></a></li><li>Tiles © <a href="http://www.esri.com/">ESRI</a></li></ul><button type="button" title="Attributions"><span>i</span></button></div></div></div></div><!-- //#emap -->

    <div class="point-forecast-map-footer">
        <img src="./images/wtf/maplegend_forecast-area.gif" width="100" height="16" alt="Map Legend">
    </div><!-- //.point-forecast-map-footer -->

</div> <!-- //.point-forecast-map -->
<!-- //forecast-map -->
        <!-- //openlayer map -->

        <!-- About this Forecast -->
        <div id="about_forecast">
            <div class="fullRow">
                <div class="left">Point Forecast:</div>
                <div class="right">San Francisco CA<br>&nbsp;37.77°N 122.41°W (Elev. 131 ft)</div>
                    </div>
            <div class="fullRow">
                <div class="left"><a target="_blank" href="//www.weather.gov/glossary/index.php?word=Last+update">Last Update</a>: </div>
                <div class="right">8:27 pm PST Feb 6, 2024</div>
            </div>
            <div class="fullRow">
                <div class="left"><a target="_blank" href="//www.weather.gov/glossary/index.php?word=forecast+valid+for">Forecast Valid</a>: </div>
                <div class="right">10pm PST Feb 6, 2024-6pm PST Feb 13, 2024</div>
            </div>
            <div class="fullRow">
                <div class="left">&nbsp;</div>
                <div class="right"><a href="https://forecast.weather.gov/product.php?site=MTR&amp;issuedby=MTR&amp;product=AFD&amp;format=CI&amp;version=1&amp;glossary=1">Forecast Discussion</a></div>
            </div>
            <div class="fullRow">
                <div class="left">&nbsp;</div>
                <div class="right">
                    <a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=kml"><img src="/images/wtf/kml_badge.png" width="45" height="17" alt="Get as KML"></a>
                    <a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=dwml"><img src="/images/wtf/xml_badge.png" width="45" height="17" alt="Get as XML"></a>
                </div>
            </div>
        </div>
        <!-- /About this Forecast -->
    </div>
    
        <!--additionalForecast-->
        <div class="panel panel-default" id="additionalForecast">
            <div class="panel-heading">
                <h2 class="panel-title">Additional Resources</h2>
            </div>
            <div class="panel-body">

                <!-- Radar & Satellite Images -->
                <div id="radar" class="subItem">
                    <h4>Radar &amp; Satellite Image</h4>
                    <a href="http://radar.weather.gov/station/kmux/standard"><img src="http://radar.weather.gov/ridge/standard/KMUX_0.gif" class="radar-thumb" alt="Link to Local Radar Data" title="Link to Local Radar Data"></a>                    <a href="https://www.star.nesdis.noaa.gov/GOES/sector.php?sat=G17&amp;sector=psw"><img src="https://cdn.star.nesdis.noaa.gov/GOES17/ABI/SECTOR/psw/GEOCOLOR/600x600.jpg" class="satellite-thumb" alt="Link to Satellite Data" title="Link to Satellite Data"></a>                </div>
                <!-- /Radar & Satellite Images -->
                <!-- Hourly Weather Forecast -->
                <div id="feature" class="subItem">
                    <h4>Hourly Weather Forecast</h4>
                    <a href="MapClick.php?lat=37.7772&amp;lon=-122.4168&amp;unit=0&amp;lg=english&amp;FcstType=graphical"><img src="newimages/medium/hourlyweather.png" class="img-responsive"></a>
                </div>
                <!-- /Hourly Weather Forecast -->
                <!-- NDFD -->
                <div id="NDFD" class="subItem">
                    <h4>National Digital Forecast Database</h4>
                    <div class="one-sixth-first"><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=MaxT"><img src="//graphical.weather.gov/images/thumbnail/latest_MaxMinT_pacsouthwest_thumbnail.png" border="0" alt="National Digital Forecast Database Maximum Temperature Forecast" title="National Digital Forecast Database Maximum Temperature Forecast" width="147" height="150"></a>
                <p><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=MaxT">High Temperature</a></p></div><div class="one-sixth-first"><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=Wx"><img src="//graphical.weather.gov/images/thumbnail/latest_Wx_pacsouthwest_thumbnail.png" border="0" alt="National Digital Forecast Database Weather Element Forecast" title="National Digital Forecast Database Weather Element Forecast" width="147" height="150"></a>
                <p><a href="//graphical.weather.gov/sectors/pacsouthwest.php?element=Wx">Chance of Precipitation</a></p></div>                </div>
                <!-- /NDFD -->
            </div>
        </div>
        <!-- /additionalForecast -->

    </div>
    <!-- /col-md-4 -->
    <!-- /right-side-data -->
    <script language="javascript">$( document ).ready(function() { load_openlayers_map('', '', '', '{"centroid_lat":"37.7772","centroid_lon":"-122.4168","lat1":"37.7595","lon1":"-122.4205","lat2":"37.781","lon2":"-122.426","lat3":"37.7855","lon3":"-122.3985","lat4":"37.764","lon4":"-122.393"}') });</script></div>
<!-- /row  -->


</div>
<!-- /PageFormat-Land -->

        
            <footer>
                        <div id="sitemap" class="sitemap-content row">
            <div class="col-xs-12">
                <div class="sitemap-columns">
                                                    <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://alerts.weather.gov">ACTIVE ALERTS</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-1">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-1">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" http://alerts.weather.gov">Warnings By State</a></li>
                                                                                                <li><a href=" http://www.wpc.ncep.noaa.gov/ww.shtml">Excessive Rainfall and Winter Weather Forecasts</a></li>
                                                                                                <li><a href="http://water.weather.gov/ahps/?current_color=flood&amp;current_type=all&amp;fcst_type=obs&amp;conus_map=d_map">River Flooding </a></li>
                                                                                                <li><a href=" http://www.weather.gov">Latest Warnings</a></li>
                                                                                                <li><a href=" http://www.spc.noaa.gov/products/outlook/">Thunderstorm/Tornado Outlook </a></li>
                                                                                                <li><a href=" http://www.nhc.noaa.gov/">Hurricanes </a></li>
                                                                                                <li><a href=" http://www.spc.noaa.gov/products/fire_wx/">Fire Weather Outlooks </a></li>
                                                                                                <li><a href=" http://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/uv_alert.shtml">UV Alerts </a></li>
                                                                                                <li><a href=" http://www.drought.gov/">Drought </a></li>
                                                                                                <li><a href="http://www.swpc.noaa.gov/products/alerts-watches-and-warnings">Space Weather </a></li>
                                                                                                <li><a href=" http://www.nws.noaa.gov/nwr/">NOAA Weather Radio </a></li>
                                                                                                <li><a href=" http://alerts.weather.gov/">NWS CAP Feeds </a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="https://www.weather.gov/wrh/climate">PAST WEATHER</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-2">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-2">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" http://www.cpc.ncep.noaa.gov/products/MD_index.shtml">Climate Monitoring </a></li>
                                                                                                <li><a href="https://www.weather.gov/wrh/climate">Past Weather </a></li>
                                                                                                <li><a href="https://www.weather.gov/wrh/climate">Monthly Temps </a></li>
                                                                                                <li><a href="https://www.weather.gov/wrh/climate">Records </a></li>
                                                                                                <li><a href="https://www.esrl.noaa.gov/gmd/grad/solcalc/sunrise.html">Astronomical Data </a></li>
                                                                                                <li><a href="https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table">Certified Weather Data </a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://www.weather.gov/current">CURRENT CONDITIONS</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-3">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-3">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" https://radar.weather.gov">Radar </a></li>
                                                                                                <li><a href="http://www.cpc.ncep.noaa.gov/products/monitoring_and_data/">Climate Monitoring </a></li>
                                                                                                <li><a href=" http://water.weather.gov/ahps/">River Levels </a></li>
                                                                                                <li><a href=" http://water.weather.gov/precip/">Observed Precipitation </a></li>
                                                                                                <li><a href="https://www.wpc.ncep.noaa.gov/sfc/sfcobs/sfcobs.shtml">Surface Weather </a></li>
                                                                                                <li><a href="http://www.spc.noaa.gov/obswx/maps/">Upper Air </a></li>
                                                                                                <li><a href=" http://www.ndbc.noaa.gov/">Marine and Buoy Reports </a></li>
                                                                                                <li><a href="http://www.nohrsc.noaa.gov/interactive/html/map.html">Snow Cover </a></li>
                                                                                                <li><a href=" http://www.weather.gov/satellite">Satellite </a></li>
                                                                                                <li><a href=" http://www.swpc.noaa.gov/">Space Weather </a></li>
                                                                                                <li><a href="http://www.weather.gov/pr">International Observations</a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://weather.gov/forecastmaps">FORECAST</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-4">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-4">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" http://www.weather.gov/">Local Forecast </a></li>
                                                                                                <li><a href="http://www.weather.gov/pr">International Forecasts</a></li>
                                                                                                <li><a href=" http://www.spc.noaa.gov/">Severe Weather </a></li>
                                                                                                <li><a href=" http://www.wpc.ncep.noaa.gov/">Current Outlook Maps </a></li>
                                                                                                <li><a href="http://www.cpc.ncep.noaa.gov/products/Drought">Drought </a></li>
                                                                                                <li><a href="http://www.weather.gov/fire">Fire Weather </a></li>
                                                                                                <li><a href=" http://www.wpc.ncep.noaa.gov/">Fronts/Precipitation Maps </a></li>
                                                                                                <li><a href=" http://www.nws.noaa.gov/forecasts/graphical/">Current Graphical Forecast Maps </a></li>
                                                                                                <li><a href="http://water.weather.gov/ahps/forecasts.php">Rivers </a></li>
                                                                                                <li><a href="https://www.weather.gov/marine/">Marine </a></li>
                                                                                                <li><a href="https://ocean.weather.gov/marine_areas.php">Offshore and High Seas</a></li>
                                                                                                <li><a href=" http://www.nhc.noaa.gov/">Hurricanes </a></li>
                                                                                                <li><a href=" http://aviationweather.gov">Aviation Weather </a></li>
                                                                                                <li><a href="http://www.cpc.ncep.noaa.gov/products/OUTLOOKS_index.shtml">Climatic Outlook </a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://www.weather.gov/informationcenter">INFORMATION CENTER</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-5">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-5">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" http://www.spaceweather.gov">Space Weather </a></li>
                                                                                                <li><a href="http://www.weather.gov/briefing/">Daily Briefing </a></li>
                                                                                                <li><a href=" http://www.nws.noaa.gov/om/marine/home.htm">Marine </a></li>
                                                                                                <li><a href="https://www.weather.gov/wrh/climate">Climate </a></li>
                                                                                                <li><a href="http://www.weather.gov/fire">Fire Weather </a></li>
                                                                                                <li><a href=" http://www.aviationweather.gov/">Aviation </a></li>
                                                                                                <li><a href="http://mag.ncep.noaa.gov/">Forecast Models </a></li>
                                                                                                <li><a href="http://water.weather.gov/ahps/">Water </a></li>
                                                                                                <li><a href="https://www.weather.gov/gis/">GIS</a></li>
                                                                                                <li><a href=" http://www.nws.noaa.gov/om/coop/">Cooperative Observers </a></li>
                                                                                                <li><a href="https://www.weather.gov/skywarn/">Storm Spotters </a></li>
                                                                                                <li><a href="http://www.tsunami.gov">Tsunami Warning System</a></li>
                                                                                                <li><a href="http://water.noaa.gov/">National Water Center</a></li>
                                                                                                <li><a href="http://www.weather.gov/pr">International Weather</a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://weather.gov/safety">WEATHER SAFETY</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-6">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-6">
                                        <ul class="list-unstyled">
                                                                                            <li><a href="http://www.weather.gov/nwr/">NOAA Weather Radio</a></li>
                                                                                                <li><a href="http://www.weather.gov/stormready/">StormReady</a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/om/heat/index.shtml">Heat </a></li>
                                                                                                <li><a href="https://www.weather.gov/safety/lightning">Lightning </a></li>
                                                                                                <li><a href=" http://www.nhc.noaa.gov/prepare/">Hurricanes </a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/om/thunderstorm/">Thunderstorms </a></li>
                                                                                                <li><a href="https://www.weather.gov/safety/tornado">Tornadoes </a></li>
                                                                                                <li><a href="https://www.weather.gov/safety/ripcurrent">Rip Currents </a></li>
                                                                                                <li><a href="https://www.weather.gov/safety/flood">Floods </a></li>
                                                                                                <li><a href="https://www.weather.gov/safety/tsunami">Tsunamis</a></li>
                                                                                                <li><a href="https://www.weather.gov/tsunamiready/">TsunamiReady</a></li>
                                                                                                <li><a href=" http://www.weather.gov/om/winter/index.shtml">Winter Weather </a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/om/heat/uv.shtml">Ultra Violet Radiation </a></li>
                                                                                                <li><a href=" http://www.weather.gov/airquality/">Air Quality </a></li>
                                                                                                <li><a href=" http://www.weather.gov/om/hazstats.shtml">Damage/Fatality/Injury Statistics </a></li>
                                                                                                <li><a href=" http://www.redcross.org/">Red Cross </a></li>
                                                                                                <li><a href=" http://www.fema.gov/">Federal Emergency Management Agency (FEMA) </a></li>
                                                                                                <li><a href=" http://www.weather.gov/om/brochures.shtml">Brochures </a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/os/marine/safeboating/">Safe Boating</a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://weather.gov/news">NEWS</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-7">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-7">
                                        <ul class="list-unstyled">
                                                                                            <li><a href=" http://weather.gov/news">Newsroom</a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/com/weatherreadynation/calendar.html">Events</a></li>
                                                                                                <li><a href=" http://www.weather.gov/om/brochures.shtml">Pubs/Brochures/Booklets </a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://weather.gov/owlie">EDUCATION</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-8">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-8">
                                        <ul class="list-unstyled">
                                                                                            <li><a href="http://weather.gov/education">NWS Education Home</a></li>
                                                                                                <li><a href="http://www.nws.noaa.gov/com/weatherreadynation/force.html">Be A Force of Nature</a></li>
                                                                                                <li><a href=" http://www.education.noaa.gov/Weather_and_Atmosphere/">NOAA Education Resources </a></li>
                                                                                                <li><a href=" http://www.weather.gov/glossary/">Glossary </a></li>
                                                                                                <li><a href="https://www.weather.gov/jetstream/">JetStream </a></li>
                                                                                                <li><a href=" http://www.weather.gov/training/">NWS Training Portal </a></li>
                                                                                                <li><a href="https://library.noaa.gov/">NOAA Library </a></li>
                                                                                                <li><a href="http://weather.gov/owlie">For Students, Parents and Teachers</a></li>
                                                                                                <li><a href="http://www.weather.gov/owlie/publication_brochures">Brochures </a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                                <div class="sitemap-section">
                                    <div class="panel-heading">
                                        <a class="sitemap-section-heading" href="http://weather.gov/about">ABOUT</a>
                                        <button type="button" class="menu-toggle pull-right" data-toggle="collapse" data-target="#sitemap-9">
                                            <span class="sr-only">Toggle menu</span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                            <span class="icon-bar"></span>
                                        </button>
                                    </div>
                                    <div class="sitemap-section-body panel-body collapsable collapse" id="sitemap-9">
                                        <ul class="list-unstyled">
                                                                                            <li><a href="http://weather.gov/organization">Organization </a></li>
                                                                                                <li><a href="https://www.noaa.gov/NWStransformation">NWS Transformation</a></li>
                                                                                                <li><a href="https://www.weather.gov/media/wrn/NWS-2023-Strategic-Plan.pdf">Strategic Plan </a></li>
                                                                                                <li><a href="https:/weather.gov/insider">For NWS Employees </a></li>
                                                                                                <li><a href="https://www.weather.gov/international/">International </a></li>
                                                                                                <li><a href="http://www.weather.gov/ncep">National Centers </a></li>
                                                                                                <li><a href=" http://www.weather.gov/tg/">Products and Services </a></li>
                                                                                                <li><a href="http://www.weather.gov/careers/">Careers</a></li>
                                                                                                <li><a href=" http://www.weather.gov/glossary/">Glossary </a></li>
                                                                                                <li><a href="http://weather.gov/contact">Contact Us </a></li>
                                                                                                <li><a href="https://weather.gov/socialmedia">Social Media</a></li>
                                                                                        </ul>
                                    </div>
                                </div>
                                                </div>
            </div>
        </div>
        
                <!-- legal footer area -->
                        <div class="footer-legal">
            <div id="footerLogo" class="col-xs-12 col-sm-2 col-md-2">
                <a href="//www.usa.gov"><img src="/css/images/usa_gov.png" alt="usa.gov" width="110" height="30"></a>
            </div>
            <div class="col-xs-12 col-sm-4 col-md-4">
                <ul class="list-unstyled footer-legal-content">
                <li><a href="//www.commerce.gov">US Dept of Commerce</a></li>
                <li><a href="//www.noaa.gov">National Oceanic and Atmospheric Administration</a></li>
                <li><a href="//www.weather.gov">National Weather Service</a></li>
                <li><a href="https://www.weather.gov/mtr">San Francisco Bay Area, CA</a></li><li><br><a href="mailto:w-mtr.webmaster@noaa.gov">Comments? Questions? Please Contact Us.</a></li>                </ul>
            </div>
            <div class="col-xs-12 col-sm-3 col-md-3">
                <ul class="list-unstyled">
                    <li><a href="https://www.weather.gov/disclaimer">Disclaimer</a></li>
                    <li><a href="//www.cio.noaa.gov/services_programs/info_quality.html">Information Quality</a></li>
                    <li><a href="https://www.weather.gov/help">Help</a></li>
                    <li><a href="//www.weather.gov/glossary">Glossary</a></li>
                </ul>
            </div>
            <div class="col-xs-12 col-sm-3 col-md-3">
                <ul class="list-unstyled">
                    <li><a href="https://www.weather.gov/privacy">Privacy Policy</a></li>
                    <li><a href="https://www.noaa.gov/foia-freedom-of-information-act">Freedom of Information Act (FOIA)</a></li>
                    <li><a href="https://www.weather.gov/about">About Us</a></li>
                    <li><a href="https://www.weather.gov/careers">Career Opportunities</a></li>
                </ul>
            </div>
        </div>
        
            </footer>
        </main>
    

<div class="autocomplete-suggestions" style="position: absolute; display: none; width: 400px; max-height: 300px; z-index: 9999;"></div>
<div id="no-view-options"></div>
</body></html>'''
def scraping_use_select(html) :
    soup = BeautifulSoup(html, 'html.parser')

    #select
    period = soup.select('.forecast-tombstone > .tombstone-container>.period-name')
    short_desc = soup.select('.short-desc')
    temp_low = soup.select(".forecast-tombstone > .tombstone-container > .temp")
    img = soup.select('.forecast-tombstone > .tombstone-container >p >img')
    for i in range(len(period)) :
        if i == 0:
            print(f'[period] :', period[i].text)
            print(f'[short_desc] : None')
            print(f'[temperature]: None')
            print(f'[img desc]: None')
            print()
        else :
            print(f'[period] :', period[i].text)
            print(f'[short_desc] :', short_desc[i-1].text)
            print(f'[temperature]:', temp_low[i-1].text)
            print(f'[img desc]:', str(img[i-1]).split('title=')[1].rstrip('"/>').lstrip('"'))
            print()

#find
def scraping_use_find(html) :
    soup = BeautifulSoup(html, 'html.parser')
    period2 = soup.find_all('p', {'class':'period-name'})
    short_desc2 = soup.find_all('p', {'class':'short-desc'})
    temperature = soup.find_all('p', {'class':'temp'})
    img2 = soup.find_all('img')[6:14]
    #for n in img2 :
        #print(n, sep='\n')

    for i in range(len(period2)) :
        if i == 0:
            print(f'[period] :', period2[i].text)
            print(f'[short_desc] : None')
            print(f'[temperature]: None')
            print(f'[img desc]: None')
            print()
        else :
            print(f'[period] :', period2[i].text)
            print(f'[short_desc] :', short_desc2[i-1].text)
            print(f'[temperature]:', temperature[i-1].text)
            print(f'[img desc]:', str(img2[i-1]).split('title=')[1].rstrip('"/>').lstrip('"'))
            print()
print('-'*100)
print('[select() 사용]')
print('-'* 100)
scraping_use_select(html_example)
print('-'* 100)
print('[find() 사용]')
print('-'* 100)
scraping_use_find(html_example)