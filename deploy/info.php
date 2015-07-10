<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'ntp';
$app['version'] = '2.1.6';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('ntp_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('ntp_app_name');
$app['category'] = lang('base_category_network');
$app['subcategory'] = lang('base_subcategory_infrastructure');

/////////////////////////////////////////////////////////////////////////////
// Controllers
/////////////////////////////////////////////////////////////////////////////

$app['controllers']['ntp']['title'] = lang('ntp_app_name');
$app['controllers']['settings']['title'] = lang('base_settings');

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['requires'] = array(
    'app-network',
);

$app['core_requires'] = array(
    'app-date-core >= 1:1.4.8',
    'app-network-core >= 1:1.4.70',
    'ntp >= 4.2.4',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/ntp' => array(),
    '/var/clearos/ntp/backup' => array(),
    '/etc/clearos/firewall.d' => array(),
);

$app['core_file_manifest'] = array(
    'ntpd.php'=> array('target' => '/var/clearos/base/daemon/ntpd.php'),
    'network-connected-event'=> array(
        'target' => '/var/clearos/events/network_connected/ntp',
        'mode' => '0755'
    ),
    '10-ntp' => array(
        'target' => '/etc/clearos/firewall.d/',
        'mode' => '0755',
    ),
);

$app['delete_dependency'] = array(
    'app-ntp-core',
    'ntp',
);
