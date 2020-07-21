# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TerritorialControl
                                 A QGIS plugin
 This plugin is an upgraded version of Territorial Control in QGIS2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-09-19
        copyright            : (C) 2019 by Ran Tao
        email                : rtao@usf.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TerritorialControl class from file TerritorialControl.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Territorial_Control import TerritorialControl
    return TerritorialControl(iface)
