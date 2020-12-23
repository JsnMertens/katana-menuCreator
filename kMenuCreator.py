#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Katana Menu creator."""

from Katana import UI4
# Qt.py from Mottosso
# https://github.com/mottosso/Qt.py
from Qt import QtWidgets

# Prefix Object Name
PREFIX_MENU_OBJECT_NAME = 'cstQMenu'


def getKatanaMainWindow():
    """Get Katana main Window.

    Returns:
        (UI4.App.MainWindow.KatanaWindow): Katana Main Window
    """
    return UI4.App.MainWindow.GetMainWindow()


def getKatanaMainMenu():
    """Get Katana main Menu.

    Returns:
        (UI4.App.MainMenu.MainMenu): Katana Main Menu
    """
    mainWindow = getKatanaMainWindow()
    return mainWindow.findChild(UI4.App.MainMenu.MainMenu)


def createMainMenu(name):
    """Create main Menu.

    Args:
        name(str): Menu name

    Returns:
        (QtWidgets.QMenu): Created Menu
    """
    menu = getKatanaMainMenu().addMenu(name)
    menu.setObjectName('{}_{}'.format(PREFIX_MENU_OBJECT_NAME, name))
    return menu


def getMainMenu(name):
    """Get main Menu.

    Args:
        name(str): Menu name

    Returns:
        (QtWidgets.QMenu): Created Menu
    """
    return getKatanaMainMenu().findChild(QtWidgets.QMenu, '{}_{}'.format(PREFIX_MENU_OBJECT_NAME, name))


def createMenu(name, parentMenu):
    """Create Menu.

    Args:
        name(str): Menu name
        parentMenu(QtWidgets.QMenu): Parent Menu

    Returns:
        (QtWidgets.QMenu): Created Menu
    """
    if not isinstance(parentMenu, QtWidgets.QMenu):
        raise TypeError('Argument has unexpected type:', type(parentMenu))

    menu = parentMenu.addMenu(name)
    menu.setObjectName('{}_{}'.format(PREFIX_MENU_OBJECT_NAME, name))
    return menu


def getMenu(name, parentMenu):
    """Get Menu.

    Args:
        name(str): Menu name
        parentMenu(QtWidgets.QMenu): Parent Menu

    Returns:
        (QtWidgets.QMenu): Menu
    """
    if not isinstance(parentMenu, QtWidgets.QMenu):
        raise TypeError('Argument has unexpected type:', type(parentMenu))

    return parentMenu.findChild(QtWidgets.QMenu, '{}_{}'.format(PREFIX_MENU_OBJECT_NAME, name))
