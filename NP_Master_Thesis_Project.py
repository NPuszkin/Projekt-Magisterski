# Importing the necessary libraries.

import os
import sys
import time
import numpy as np
import pandas as pd
import plotly.colors as pc
import plotly.graph_objects as go
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from scipy.signal import argrelextrema

# Showing program logo for 2 seconds before Choose File window appears.

app_logo = QApplication(sys.argv)
show_logo = QSplashScreen(QtGui.QPixmap('Images/N.png'))
show_logo.show()
time.sleep(2)
show_logo.close()

# Class HelpWindow - creating window, that appears after choosing Help from Menu Bar in Main Window.
# It contains short user guide, which may be helpful in understanding the functions of the program.
# It is build using labels and images.


class HelpWindow(QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()

        self.setFixedSize(780, 650)
        self.setWindowTitle("Help")
        self.setWindowIcon(QtGui.QIcon('Images/help-icon.png'))

        self.scrollAreaHelp = QScrollArea(self)
        self.scrollAreaHelp.setGeometry(QtCore.QRect(0, 0, 781, 651))
        self.scrollAreaHelp.setWidgetResizable(True)
        self.scrollAreaHelp.setStyleSheet("background-color: white")
        self.scrollAreaHelpWidgetContents_2 = QWidget()
        self.scrollAreaHelpWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 649))
        self.scrollAreaHelp.setWidget(self.scrollAreaHelpWidgetContents_2)

        self.layHelp = QVBoxLayout(self.scrollAreaHelpWidgetContents_2)

        self.labelUserGuide = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.labelUserGuide.setGeometry(QtCore.QRect(150, 20, 321, 51))
        self.labelUserGuide.setText("\nShort User Guide ")
        self.labelUserGuide.setStyleSheet("background-color: white; text-align: top;")
        self.labelUserGuide.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                          "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.labelUserGuide)

        self.label_1header = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.label_1header.setText("\n\n1. Input files\n\n")
        self.label_1header.setStyleSheet("background-color: white; text-align: top;")
        self.label_1header.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                         "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.label_1header)

        self.labelHelp = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.labelHelp.setText("As you were informed in the start window, you need files with extention:\n"
                               "case.qtl, case.spaghetti_ene and case.klist_band to use the program.\n\n"
                               "a) case.qtl\n\nThe program uses the data collected in the case.qtl file in order "
                               "to collect energy data,\nas well as display information about the analyzed compound, "
                               "such as Fermi energy,\nlattice constants and orbitals share. Also, band "
                               "structures plots with band character\nare generated on the basis of the data "
                               "from this file.\n\nb) case.spaghetti_ene\n\nThe case.spaghetti_ene file provides "
                               "the k-path, which is necessary\nto generate band structure plots.\n\n"
                               "c) case.klist_band\n\nWith this file, the program collects the coordinates "
                               "of the k vector to display them\non the charts of the band structure.\nAdditionally "
                               "the program uses the high symmetry points, contained in this file,\n"
                               "to generate an appropriate legend of the charts.")

        self.labelHelp.setStyleSheet("background-color: white; text-align: top;")

        self.labelHelp.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                     "color: black; qproperty-alignment: 'AlignCenter';")

        self.layHelp.addWidget(self.labelHelp)

        self.label_2header = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.label_2header.setText("\n\n2. Main window\n\n")
        self.label_2header.setStyleSheet("background-color: white; text-align: top;")
        self.label_2header.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                         "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.label_2header)

        self.labelHelp = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.labelHelp.setText(
            "There are three items in the bar menu - File, Help and Info. The first of them - File,\n"
            "contains the option to load a new file "
            "('New ...'), thus opening the program's start window,\nclosing the current window. "
            "Moreover, it allows you to close the program ('Exit').\nAfter selecting Help, this "
            "window appears. Info opens a window with information\nabout the project within which "
            "the program was created and its author.\n\nThen in the main window there is a fragment "
            "containing information about the compound,\ncollected on the basis of a file with the"
            "extension case.qtl - compound name ('Compound'),\nFermi energy ('Fermi Energy'), "
            "lattice constants ('Lattice constants [bohr]') and data on\nnon-equivalent atoms "
            "('Atoms Info')."
            "\n\nThe user has the option to choose the energy unit in which he wants to generate\n"
            "the band structure ('Choose energy unit'). Information about the highest "
            "('Maximum energy')\nand the lowest ('Minimum energy') is also displayed. "
            "When selecting the Rydbergs as the unit,\nthe option appears to shift the Fermi level "
            "to zero ('Fermi Energy to 0'). The minimum and\nmaximum energy values also "
            "change accordingly. For a band structure where the selected \nenergy unit is "
            "an electron volt, the Fermi level is always shifted to zero.\n\n"
            "In the main window, it is possible to enter the desired energy range on the band\n"
            "structure plot - 'Input Energy range (optional)'. Omitting this option results in "
            "obtaining a\nplot of the full range of available energy. The program also checks the "
            "data entered\ninto the text area - it displays messages when errors are detected, e.g.:\n")

        self.labelHelp.setStyleSheet("background-color: white; text-align: top;")

        self.labelHelp.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                     "color: black; qproperty-alignment: 'AlignCenter';")

        self.layHelp.addWidget(self.labelHelp)

        self.label_1PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/1.png')
        self.label_1PNG.setPixmap(pixmap)
        self.label_1PNG.resize(pixmap.width(), pixmap.height())
        self.label_1PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_1PNG)

        self.label_2PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/2.png')
        self.label_2PNG.setPixmap(pixmap)
        self.label_2PNG.resize(pixmap.width(), pixmap.height())
        self.label_2PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_2PNG)

        self.label_3header = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.label_3header.setText("\n2.1 Band structure plots\n")
        self.label_3header.setStyleSheet("background-color: white; text-align: top;")
        self.label_3header.setStyleSheet("font: 9.5pt \"MS Shell Dlg 2\";\n"
                                         "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.label_3header)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("The first of the possibilities of the program is to plot the band structure in "
                                "the selected\nenergy unit and its entered range. The 'Draw band structure' button "
                                "is responsible for this.\nThe graphs are generated on the basis of a set of "
                                "points - energy values and\nthe corresponding values of the vector path k. "
                                "An example of such a graph (TiC2):\n")
        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_3PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/3.png')
        self.label_3PNG.setPixmap(pixmap)
        self.label_3PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_3PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nBand structure plots have been equipped with an update menu that allows the user"
                                "\nto adjust their appearance according to his preferences.\n\nParameters that "
                                "can be changed:\na) bands color - to choose from: cornflowerblue, mediumseagreen, "
                                "darkslategray, darkgoldenrod,\nb) chart background color - to choose from: "
                                "white, ivory, whitesmoke, snow,\nc) line thickness - to choose from: 1, 1.5, 2, "
                                "2.5, 3, 3.5,\nd) visibility of the legend.\nIf you click on the label of a "
                                "given band in the legend, it is no longer visible.\nAfter double-clicking on such "
                                "a mark, only the selected band remains on the graph.\nHovertext that appears after "
                                "hovering the cursor over the graph points contains information\nabout the energy value, "
                                "the k-vector coordinates, as well as the band number.")
        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_4header = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.label_4header.setText("\n2.2 Band structure plots with effective mass\n")
        self.label_4header.setStyleSheet("background-color: white; text-align: top;")
        self.label_4header.setStyleSheet("font: 9.5pt \"MS Shell Dlg 2\";\n"
                                         "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.label_4header)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("The written program makes it possible to calculate the effective mass. For this "
                                "purpose,\nit looks for local extremes for each band, and also performs a quadratic "
                                "interpolation on the\nbasis of the nearest ten points (five with lower indices "
                                "and five with indexes higher than\nthe index of the found extreme). For extremes "
                                "for which such interpolation cannot be performed\n(which is the case when the extremum "
                                "is near the beginning or end of the band and there are not\nenough adjacent points), "
                                "the coefficients of the second order polynomial are calculated taking into\naccount "
                                "only the two closest points - i.e. a point with an index one higher and one lower.\n"
                                "The graph of the band structure with effective mass is obtained by pressing the "
                                "'Effective mass'\nbutton in the main window. To list the points for which the "
                                "effective mass is calculated, underline\nthem by adding dot marks. from the index "
                                "of the found extreme. Sample plot (TiC2):\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_4PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/4.png')
        self.label_4PNG.setPixmap(pixmap)
        self.label_4PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_4PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nThis kind of plot also has an update menu. Plot personalization is possible through:"
                                "\na) changing the color of the bands, to choose from: cornflowerblue, mediumseagreen,"
                                "\ndarkslategray, darkgoldenrod,\nb) change the color of the markers indicating the "
                                "position of the points for which the effective mass\nis calculated, to choose from: "
                                "darkcyan, forestgreen, black, saddlebrown, purple, maroon,\nc) changing the background "
                                "color of the chart: white, ivory, whitesmoke, snow,\nd) change the line thickness - "
                                "to choose from: 1, 1.5, 2, 2.5, 3, 3.5,\ne) hide the legend.\n\nThe label for this type "
                                "of graphs differs from the label for band structures in that it has an additional\n"
                                "line at the beginning, which for the points constituting local band extremes contains "
                                "the effective\nmass calculated for them.")
        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_5header = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.label_5header.setText("\n2.3 Band structure plots with band character\n")
        self.label_5header.setStyleSheet("background-color: white; text-align: top;")
        self.label_5header.setStyleSheet("font: 9.5pt \"MS Shell Dlg 2\";\n"
                                         "color: black; qproperty-alignment: 'AlignCenter'; font-weight: bold")

        self.layHelp.addWidget(self.label_5header)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nThe main window has a scroll area with check boxes that represent the names of the "
                                "orbitals.\nOn the basis of the orbitals selected by the user, it is possible to plot "
                                "the band structure with band\ncharacter, by pressing the 'Character' button. "
                                "The program performs this function in two ways.\n\n"
                                "The first is to show the band character on the basis of the marker size "
                                "in the chart - the\n'Marker size' option. Such graphs can be created only on the "
                                "basis of one selected orbital, therefore,\nwhen the 'Marker size' option is selected, "
                                "the program does not allow selecting more orbitals.\nSample diagram (TiC2):\n")
        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_5PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/5.png')
        self.label_5PNG.setPixmap(pixmap)
        self.label_5PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_5PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nHovertext, in addition to information about the energy value for a given point, "
                                "k-vector coordinates\nand band number, contains the name of the selected orbital and "
                                "its share. The larger the point,\nthe greater the share of a given orbital in the band, "
                                "the point size is obtained by multiplying\nthe share obtained from the file with the "
                                "case.qtl extension by the multiplier selected by the user\nfrom the 'Marker size "
                                "multiplier' field (to choose from: 3, 5, 10 , 15). This solution allows for\na better "
                                "visualization of the band character, especially in the case of orbitals with a low "
                                "share.\n\nThe update menu for this type of chart has the following options:"
                                "\na) changes in the color of the bands, to choose from: cornflowerblue, mediumseagreen,"
                                " darkslategray, darkgoldenrod,\nb) changing the background color of the chart, to "
                                "choose from: white, ivory, whitesmoke, snow,\nc) change the color of markers, to "
                                "choose from: royalblue, seagreen, black, saddlebrown,\nd) change the color of the "
                                "marker border, to choose from: royalblue, seagreen, black, saddlebrown,\ne) hide the "
                                "legend.\n\n"
                                "The second way to present the nature of the bands, which allows the written program, "
                                "is to\ngenerate a graph in which the color of the point indicates the share of a "
                                "given orbital - this option\nis available after selecting 'Color' from the main "
                                "window. For this purpose, you can select up to\nthree orbitals for which the user "
                                "wants to show the character. Hovertext is the same as for band\nstructure plots showing"
                                " band character by marker size. Sample plot (TiC2):\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_6PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/6.png')
        self.label_6PNG.setPixmap(pixmap)
        self.label_6PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_6PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nThe color of the point reflects the orbital contribution according to the legend "
                                "of the color bar.\nThe top menu is equipped with the possibility of:\n"
                                "a) selecting the type of chart as markers, or markers + lines,\nb) changing the "
                                "colorscale, to choose from: black-red, black-green, black-blue,\nc) changes in the "
                                "upper limit of the color, to choose from: max (the maximum share of a given\n"
                                "orbital) or 1 (such a graph is presented in below for comparison, it is a useful "
                                "option to see how\nthe share of a given orbital compares to the whole),\nd) changing "
                                "the background color of the chart, to choose from: white, ivory, whitesmoke, snow.\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_7PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/7.png')
        self.label_7PNG.setPixmap(pixmap)
        self.label_7PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_7PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nIf two or three orbitals are selected, the color of the point is obtained by "
                                "normalizing the shares\nof that orbital - scaling them so that the values of the "
                                "shares range from zero to one, then\nmultiplying these values by 255 to get the "
                                "individual RGB color components.\n\nThe band structure plot with band character"
                                " based on two selected orbitals:\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_8PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/8.png')
        self.label_8PNG.setPixmap(pixmap)
        self.label_8PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_8PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nThe band structure plot with band character"
                                " based on three selected orbitals:\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")
        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

        self.label_9PNG = QLabel(self.scrollAreaHelpWidgetContents_2)
        pixmap = QtGui.QPixmap('Images/9.png')
        self.label_9PNG.setPixmap(pixmap)
        self.label_9PNG.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.label_9PNG)

        self.next_label = QLabel(self.scrollAreaHelpWidgetContents_2)
        self.next_label.setText("\nIn the bottom right corner there is a legend indicating which color corresponds "
                                "to which orbital.\n\nThe update menu of these charts includes the ability to:"
                                "\na) selecting the type of chart as markers, or markers + lines,\nb) changing "
                                "the background color of the chart, to choose from: white, ivory, whitesmoke, snow,\n"
                                "c) change the size of markers, to choose from: 4, 5, 6, 7,\nd) hide the legend.\n")

        self.next_label.setStyleSheet("background-color: white; text-align: top;")

        self.next_label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                      "color: black; qproperty-alignment: 'AlignCenter';")

        self.next_label.setAlignment(Qt.AlignCenter)
        self.layHelp.addWidget(self.next_label)

# Class InfoWindow - creating the window, which appears after choosing Info from Menu Bar in Main Window.
# This window contains basic information of the project and its author.


class InfoWindow(QMainWindow):
    def __init__(self):
        super(InfoWindow, self).__init__()

        self.setFixedSize(618, 373)
        self.setWindowTitle("Info")
        self.setWindowIcon(QtGui.QIcon('Images/info-icon.jpg'))
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 20, 541, 261))
        self.label.setText("Program was created as a part of master's thesis: \n\n 'Development of a Python computer "
                           "program for analysis of band structures\nobtained in ab initio calculations with WIEN2K'"
                           "\n\nAcademic year: 2020/2021"
                           "\n\nUniversity: AGH University of Science and Technology"
                           "\nFaculty: Faculty of Materials Science and Ceramics"
                           "\n\nAuthor: Natalia Puszkin"
                           "\n\nThesis Supervisor: Prof. Andrzej Koleżyński"
                           "\n\nContact: puszkin@student.agh.edu.pl")

        self.label.setStyleSheet("font: 8.5pt \"MS Shell Dlg 2\";\n"
                                 "color: black; qproperty-alignment: 'AlignCenter';")

        self.logo_agh_label = QLabel(self)
        self.logo_agh_label.setGeometry(QtCore.QRect(430, 280, 101, 81))
        self.logo_agh_label.setStyleSheet("image: url(Images/logo-agh.png);")

        self.logo_wimic_label = QLabel(self)
        self.logo_wimic_label.setGeometry(QtCore.QRect(90, 290, 101, 61))
        self.logo_wimic_label.setStyleSheet("image: url(Images/logo-wimic.jpg);")

        self.setStyleSheet("background-color: white")

# Creating the Main Window. Here all the components such labels, scroll areas, and edit lines are added.
# At this point, only the window frame is created and it does not contain any information so far.


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('Images/N.png'))
        self.setWindowTitle("Main Window")

        self.central()
        self.initUI()
        self.setFixedSize(784, 865)

    def central(self):
        cen = self.frameGeometry()
        cent = QDesktopWidget().availableGeometry().center()
        cen.moveCenter(cent)

    def initUI(self):
        self.compound_label = QLabel(self)
        self.compound_label.setGeometry(QtCore.QRect(30, 30, 731, 41))
        self.font_style()

        self.lattice_constants_label = QLabel(self)
        self.lattice_constants_label.setGeometry(QtCore.QRect(30, 90, 241, 41))
        self.lattice_constants_label.setText("Lattice constants [bohr]:    a =")
        self.font_style()

        self.maximum_energy_label = QLabel(self)
        self.maximum_energy_label.setGeometry(QtCore.QRect(30, 310, 141, 41))
        self.maximum_energy_label.setText("Maximum energy:")
        self.font_style()

        self.atoms_info_label = QLabel(self)
        self.atoms_info_label.setGeometry(QtCore.QRect(30, 130, 241, 41))
        self.atoms_info_label.setText("Atoms info:")
        self.font_style()

        self.minimum_energy_label = QLabel(self)
        self.minimum_energy_label.setGeometry(QtCore.QRect(400, 310, 141, 41))
        self.minimum_energy_label.setText("Minimum energy:")
        self.font_style()

        self.input_energy_range_label = QLabel(self)
        self.input_energy_range_label.setGeometry(QtCore.QRect(30, 370, 241, 41))
        self.input_energy_range_label.setText("Input energy range (optional):")
        self.font_style()

        self.highest_label = QLabel(self)
        self.highest_label.setGeometry(QtCore.QRect(280, 370, 71, 41))
        self.highest_label.setText("Highest:")
        self.font_style()

        self.energy_unit_label = QLabel(self)
        self.energy_unit_label.setGeometry(QtCore.QRect(30, 260, 161, 41))
        self.energy_unit_label.setText("Choose energy unit:")
        self.font_style()

        self.fermi_energy_label = QLabel(self)
        self.fermi_energy_label.setGeometry(QtCore.QRect(390, 30, 361, 41))
        self.font_style()

        self.scrollArea_2 = QScrollArea(self)
        self.scrollArea_2.setGeometry(QtCore.QRect(130, 140, 631, 111))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setStyleSheet("background-color: white")
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 609, 89))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.lay = QVBoxLayout(self.scrollAreaWidgetContents_2)

        self.label_atom_info = QLabel(self.scrollAreaWidgetContents_2)
        self.label_atom_info.setGeometry(QtCore.QRect(30, 130, 241, 41))
        self.font_style()
        self.label_atom_info.setStyleSheet("background-color: white; text-align: top;")
        self.lay.addWidget(self.label_atom_info)

        self.fermi_to_0_box = QGroupBox(self)
        self.fermi_to_0_box.setGeometry(QtCore.QRect(550, 260, 171, 41))
        self.fermi_to_0_box.setTitle("")
        self.fermi_to_0_box.hide()

        self.fermi_no_button = QRadioButton(self.fermi_to_0_box)
        self.fermi_no_button.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.fermi_no_button.setText("No")
        self.font_style()
        self.fermi_no_button.setChecked(True)

        self.fermi_yes_button = QRadioButton(self.fermi_to_0_box)
        self.fermi_yes_button.setGeometry(QtCore.QRect(20, 10, 61, 20))
        self.fermi_yes_button.setText("Yes")
        self.font_style()

        self.energy_unit_box = QGroupBox(self)
        self.energy_unit_box.setGeometry(QtCore.QRect(190, 260, 171, 41))
        self.energy_unit_box.setTitle("")

        self.energy_eV = QRadioButton(self.energy_unit_box)
        self.energy_eV.setGeometry(QtCore.QRect(20, 10, 61, 20))
        self.energy_eV.setText("Ev")
        self.font_style()
        self.energy_eV.setChecked(True)
        self.energy_eV.clicked.connect(self.hide_fermi_to_0)

        self.energy_Ry = QRadioButton(self.energy_unit_box)
        self.energy_Ry.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.energy_Ry.setText("Ry")
        self.font_style()
        self.energy_Ry.clicked.connect(self.show_fermi_to_0)

        self.fermi_to_0_label = QLabel(self)
        self.fermi_to_0_label.setGeometry(QtCore.QRect(400, 270, 161, 21))
        self.fermi_to_0_label.setText("Fermi energy to 0:")
        self.font_style()
        self.fermi_to_0_label.hide()

        self.lowest_label = QLabel(self)
        self.lowest_label.setGeometry(QtCore.QRect(530, 370, 71, 41))
        self.lowest_label.setText("Lowest:")
        self.font_style()

        self.maximum_energy_line = QLineEdit(self)
        self.maximum_energy_line.setGeometry(QtCore.QRect(190, 310, 151, 41))
        self.maximum_energy_line.setReadOnly(True)
        self.font_style()
        self.maximum_energy_line.setAlignment(QtCore.Qt.AlignCenter)

        self.minimum_energy_line = QLineEdit(self)
        self.minimum_energy_line.setGeometry(QtCore.QRect(560, 310, 151, 41))
        self.minimum_energy_line.setReadOnly(True)
        self.font_style()
        self.minimum_energy_line.setAlignment(QtCore.Qt.AlignCenter)

        self.lattice_a_line = QLineEdit(self)
        self.lattice_a_line.setGeometry(QtCore.QRect(280, 90, 111, 41))
        self.lattice_a_line.setReadOnly(True)
        self.font_style()
        self.lattice_a_line.setAlignment(QtCore.Qt.AlignCenter)

        self.lattice_c_line = QLineEdit(self)
        self.lattice_c_line.setGeometry(QtCore.QRect(650, 90, 111, 41))
        self.lattice_c_line.setReadOnly(True)
        self.font_style()
        self.lattice_c_line.setAlignment(QtCore.Qt.AlignCenter)

        self.lattice_b_line = QLineEdit(self)
        self.lattice_b_line.setGeometry(QtCore.QRect(470, 90, 101, 41))
        self.lattice_b_line.setReadOnly(True)
        self.font_style()
        self.lattice_b_line.setAlignment(QtCore.Qt.AlignCenter)

        self.highest_input_line = QLineEdit(self)
        self.highest_input_line.setGeometry(QtCore.QRect(360, 380, 151, 41))
        self.font_style()
        self.highest_input_line.setAlignment(QtCore.Qt.AlignCenter)

        self.lowest_input_line = QLineEdit(self)
        self.lowest_input_line.setGeometry(QtCore.QRect(600, 380, 151, 41))
        self.font_style()
        self.lowest_input_line.setAlignment(QtCore.Qt.AlignCenter)

        self.b_lattice_label = QLabel(self)
        self.b_lattice_label.setGeometry(QtCore.QRect(420, 90, 31, 41))
        self.b_lattice_label.setText("b =")
        self.font_style()

        self.c_lattice_label = QLabel(self)
        self.c_lattice_label.setGeometry(QtCore.QRect(600, 90, 31, 41))
        self.c_lattice_label.setText("c =")
        self.font_style()

        self.draw_band_structure_button = QPushButton(self)
        self.draw_band_structure_button.setGeometry(QtCore.QRect(60, 490, 281, 61))
        self.draw_band_structure_button.setText("Draw band structure")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.draw_band_structure_button.setFont(font)
        self.draw_band_structure_button.setStyleSheet("background-color: rgb(180, 194, 198);")

        self.effective_mass_button = QPushButton(self)
        self.effective_mass_button.setGeometry(QtCore.QRect(430, 490, 281, 61))
        self.effective_mass_button.setText("Effective mass")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.effective_mass_button.setFont(font)
        self.effective_mass_button.setStyleSheet("background-color: rgb(180, 194, 198);")

        self.info_plotly_label = QLabel(self)
        self.info_plotly_label.setGeometry(QtCore.QRect(20, 430, 741, 61))
        self.info_plotly_label.setText("Note! Plots open in web browser, "
                                       "but no internet connection is required to use the program.")
        self.info_plotly_label.setStyleSheet("font: italic 8pt \"MS Shell Dlg 2\";\n"
                                             "color: black; qproperty-alignment: 'AlignCenter';")

        self.menu_Bar = QMenuBar(self)
        self.menu_Bar.setGeometry(QtCore.QRect(0, 0, 800, 26))

        self.file_menu = self.menu_Bar.addMenu("File")

        self.help_window = HelpWindow()
        self.info_window = InfoWindow()

        self.help_menu_action = QAction(self.menu_Bar)
        self.help_menu_action.setIcon(QtGui.QIcon('Images/help-icon.png'))
        self.help_menu_action.triggered.connect(self.help_clicked)
        self.menu_Bar.addAction(self.help_menu_action)

        self.help_menu_action2 = QAction(self.menu_Bar)
        self.help_menu_action2.setText("Help")
        self.help_menu_action2.triggered.connect(self.help_clicked)
        self.menu_Bar.addAction(self.help_menu_action2)

        self.info_menu_action = QAction(self.menu_Bar)
        self.info_menu_action.setIcon(QtGui.QIcon('Images/info-icon.jpg'))
        self.info_menu_action.triggered.connect(self.info_clicked)
        self.menu_Bar.addAction(self.info_menu_action)

        self.info_menu_action2 = QAction(self.menu_Bar)
        self.info_menu_action2.setText("Info")
        self.info_menu_action2.triggered.connect(self.info_clicked)
        self.menu_Bar.addAction(self.info_menu_action2)

        self.new_file_action = QAction(self.menu_Bar)
        self.new_file_action.setText("New...")
        self.new_file_action.setIcon(QtGui.QIcon('Images/open-file-icon.png'))
        self.file_menu.addAction(self.new_file_action)

        self.file_menu.addSeparator()

        self.close_program_action = QAction(self.menu_Bar)
        self.close_program_action.setText("Close")
        self.close_program_action.setIcon(QtGui.QIcon('Images/close-icon.png'))
        self.file_menu.addAction(self.close_program_action)
        self.close_program_action.triggered.connect(QApplication.instance().quit)

        self.scrolling = QScrollArea(self)
        self.scrolling.setGeometry(QtCore.QRect(40, 640, 391, 151))
        self.scrolling.setWidgetResizable(True)
        self.scrolling.setStyleSheet("background-color: white")
        self.scrollContents = QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 389, 149))
        self.scrolling.setWidget(self.scrollContents)

        self.layying = QVBoxLayout(self.scrollContents)

        self.orbitals_group_box = QGroupBox(self.scrollContents)
        self.orbitals_group_box.setGeometry(QtCore.QRect(20, 10, 351, 131))
        self.orbitals_group_box.setTitle("")
        self.orbitals_group_box.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                              "color: black")
        self.layying2 = QVBoxLayout(self.orbitals_group_box)
        self.layying2.addStretch(1)

        self.layying.addWidget(self.orbitals_group_box)

        self.heading = QLabel(self)
        self.heading.setGeometry(QtCore.QRect(460, 590, 300, 80))
        self.heading.setText("One orbital is needed to draw character<br>based on marker size.<br>"
                             "By selecting color mode, you can select<br>up to 3 orbitals.")
        self.heading.setStyleSheet("font: italic 8pt \"MS Shell Dlg 2\";\n"
                                             "color: black; qproperty-alignment: 'AlignCenter';")

        self.heading.setAlignment(QtCore.Qt.AlignCenter)

        self.choosing_mode = QGroupBox(self)
        self.choosing_mode.setGeometry(QtCore.QRect(30, 590, 391, 41))
        self.choosing_mode.setTitle("")

        self.char_marker_size = QRadioButton(self.choosing_mode)
        self.char_marker_size.setGeometry(QtCore.QRect(40, 10, 111, 20))
        self.char_marker_size.setText("Marker size")
        self.font_style()

        self.color = QRadioButton(self.choosing_mode)
        self.color.setGeometry(QtCore.QRect(230, 10, 121, 20))
        self.color.setText("Color")
        self.font_style()

        self.draw_character = QPushButton(self)
        self.draw_character.setGeometry(QtCore.QRect(470, 680, 281, 61))
        self.draw_character.setText("Character")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.draw_character.setFont(font)
        self.draw_character.setStyleSheet("background-color: rgb(180, 194, 198);")

        self.line_middle = QFrame(self)
        self.line_middle.setGeometry(QtCore.QRect(20, 430, 731, 20))
        # self.line.setStyleSheet("")
        self.line_middle.setFrameShape(QFrame.HLine)
        self.line_middle.setFrameShadow(QFrame.Sunken)

        self.line_top = QFrame(self)
        self.line_top.setGeometry(QtCore.QRect(30, 60, 731, 16))
        self.line_top.setFrameShape(QFrame.HLine)
        self.line_top.setFrameShadow(QFrame.Sunken)

        self.line_bottom = QFrame(self)
        self.line_bottom.setGeometry(QtCore.QRect(30, 560, 721, 21))
        self.line_bottom.setFrameShape(QFrame.HLine)
        self.line_bottom.setFrameShadow(QFrame.Sunken)

        self.logo_agh_label = QLabel(self)
        self.logo_agh_label.setGeometry(QtCore.QRect(670, 760, 91, 61))
        self.logo_agh_label.setStyleSheet("image: url(Images/logo-agh.png);")

        self.master_thesis_label = QLabel(self)
        self.master_thesis_label.setGeometry(QtCore.QRect(500, 770, 180, 51))
        self.master_thesis_label.setText("The program was created<br>as part of a master's thesis.<br>2021")
        self.master_thesis_label.setStyleSheet("font: italic 8pt \"MS Shell Dlg 2\";\n"
                                             "color: black; qproperty-alignment: 'AlignCenter';")

        self.marker_size_multiplier_label = QLabel(self)
        self.marker_size_multiplier_label.setGeometry(QtCore.QRect(40, 800, 201, 41))
        self.marker_size_multiplier_label.setText("Marker size multiplier:")
        self.marker_size_multiplier_label.setFont(font)

        self.multiplier_box = QGroupBox(self)
        self.multiplier_box.setGeometry(QtCore.QRect(220, 800, 221, 41))

        self.three_button = QRadioButton(self.multiplier_box)
        self.three_button.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.three_button.setText("3")
        self.font_style()
        self.three_button.setChecked(True)

        self.five_button = QRadioButton(self.multiplier_box)
        self.five_button.setGeometry(QtCore.QRect(60, 10, 61, 20))
        self.five_button.setText("5")
        self.font_style()

        self.ten_button = QRadioButton(self.multiplier_box)
        self.ten_button.setGeometry(QtCore.QRect(110, 10, 61, 20))
        self.ten_button.setText("10")
        self.font_style()

        self.fifteen_button = QRadioButton(self.multiplier_box)
        self.fifteen_button.setGeometry(QtCore.QRect(170, 10, 61, 20))
        self.fifteen_button.setText("15")
        self.font_style()

    def font_style(self):
        font = self.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                  "color: black")
        self.font()

    def show_fermi_to_0(self):
        self.fermi_to_0_box.show()
        self.fermi_to_0_label.show()

    def hide_fermi_to_0(self):
        self.fermi_to_0_box.hide()
        self.fermi_to_0_label.hide()

    def help_clicked(self):
        self.help_window.show()

    def info_clicked(self):
        self.info_window.show()

# Class FirstWindow - creating window responsible for uploading files.
# Function of this window are used to extract data from the input files.


class FirstWindow(QMainWindow):

    def __init__(self):
        super(FirstWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('Images/N.png'))
        self.setWindowTitle("Start window")

        self.central()
        self.initUI()
        self.setFixedSize(784, 295)
        font = QtGui.QFont()
        font.setWeight(50)
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def central(self):
        cen = self.frameGeometry()
        cent = QDesktopWidget().availableGeometry().center()
        cen.moveCenter(cent)

    def initUI(self):

        self.choose_files = QPushButton(self)
        self.choose_files.setGeometry(QtCore.QRect(80, 40, 281, 61))
        self.choose_files.setText("Choose files")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.choose_files.setFont(font)
        self.choose_files.setStyleSheet("background-color: rgb(180, 194, 198);")
        self.choose_files.clicked.connect(self.open_files)

        self.progress_Bar = QProgressBar(self)
        self.progress_Bar.setGeometry(QtCore.QRect(40, 140, 721, 31))
        self.progress_Bar.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(120, 112, 136);")
        self.progress_Bar.setProperty("value", 0)

        info_label = QLabel(self)
        info_label.setText("Required files with the extension: case.qtl, <br>case.spaghetti_ene, case.klist_band. "
                           "<br>You have to wait until the progress is 100%. "
                           "<br>Sometimes it may take a while.")
        info_label.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                 "color:#000000; font-style: italic;"
                                 "qproperty-alignment: 'AlignCenter';")
        info_label.setGeometry(QtCore.QRect(390, 30, 331, 91))

        quit_button = QPushButton(self)
        quit_button.setGeometry(QtCore.QRect(80, 200, 281, 61))
        quit_button.setText("Quit window")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        quit_button.setFont(font)
        quit_button.setStyleSheet("background-color: rgb(180, 194, 198);")
        quit_button.clicked.connect(QApplication.instance().quit)

        self.next_button = QPushButton(self)
        self.next_button.setGeometry(QtCore.QRect(420, 200, 281, 61))
        self.next_button.setText("Next >>>")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("background-color: rgb(180, 194, 198);")
        self.next_button.hide()
        self.next_button.clicked.connect(self.next_button_clicked)

        # This dialog enables data transfer between windows, so extracted data from input files
        # can be used in Main Window.

        self.dialog = SecondWindow()

    def closeEvent(self, action):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            action.accept()
        if reply == QMessageBox.No:
            action.ignore()

    def open_files(self):

        # Open files function extracts data from input files.
        # Progress of this is showed by Progress Bar.

        self.next_button.hide()

        # Some variables needs to be global, so they can be passed to other functions in this class.

        global lattice_a, lattice_b, lattice_c, info_atoms_text, fermi_Energy
        global min_energy_in_eV, max_energy_in_eV, min_energy_in_Ry, max_energy_in_Ry
        global k_path, energy_df, k_vec, legend_values, high_symmetry_points, energy
        global share_of_the_orbitals_of_atoms
        global compound_name

        self.dialog.energy_eV.setChecked(True)
        self.dialog.lowest_input_line.setText("")
        self.dialog.highest_input_line.setText("")
        self.dialog.close()
        self.progress_Bar.setValue(0)

        # Unicodes for high symmetry points and orbitals names.

        unicodes = {
            'Gamma': '\u0393',
            'GAMMA': '\u0393',
            'LAMBDA': '\u039B',
            'Lambda': '\u039B',
            'DELTA': 'D',
            'Delta': 'D',
            '0': 'S',
            '1': 'P',
            '2': 'D',
            '3': 'F'
        }

        # File selection dialog, enables to choose file with extension: *.spaghetti_ene *.klist_band *.qtl.

        spaghetti_path = r''
        qtl_path = r''
        klist_band_path = r''

        filters = "Wien2k files (*.spaghetti_ene *.klist_band *.qtl);;PDF (*.pdf)"

        file_names = QFileDialog.getOpenFileNames(self, "Open file", "", filters)

        if len(file_names[0]) == 3:
            for file in file_names[0]:
                if file.endswith('spaghetti_ene'):
                    spaghetti_path += file
                if file.endswith('qtl'):
                    qtl_path += file
                if file.endswith('klist_band'):
                    klist_band_path += file
        elif len(file_names[0]) > 3:
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Too many files selected.\n'
                                 'Please select only required files.')
            error_dialog.exec_()

        # Compound name is collected from file name.

        compound_name = os.path.splitext(os.path.basename(qtl_path))[0]

        # PREPARING QTL DATA

        try:
            with open(qtl_path, 'r+') as f:
                qtl_data = f.read()

            qtl_data_split = ""

            for line in qtl_data.splitlines():
                line = line.strip()
                qtl_data_split += (line + "\n")

            qtl_data_bands = qtl_data_split.split('BAND')

            # qtl_data_heading allows to get information about the compound, atoms, orbitals.

            qtl_data_heading = qtl_data_bands[0].split()

            prepare_energy_data = {}

            for i in range(1, len(qtl_data_bands)):
                after_splitting = qtl_data_bands[i].splitlines()
                prepare_energy_data[f'Band {i}'] = after_splitting

            # Here dictionary which contains energy in Ry is created. Keys = bands.

            dict_all_energies = {}

            for i in range(1, len(prepare_energy_data.keys()) + 1):
                dict_all_energies[f'Band {i}'] = []
            for band in prepare_energy_data.keys():
                for j in prepare_energy_data[band]:
                    dict_all_energies[band].append(j.split()[0])

            for i in range(0, 21):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            const_index = qtl_data_heading.index('CONST.=')
            lattice_a = float(qtl_data_heading[const_index + 1])
            lattice_b = float(qtl_data_heading[const_index + 2])
            lattice_c = float(qtl_data_heading[const_index + 3])

            energy_index = qtl_data_heading.index('ENERGY=')
            fermi_Energy = float(qtl_data_heading[energy_index + 1])

            number_of_atoms_index = qtl_data_heading.index('NAT=')
            number_of_atoms = int(qtl_data_heading[number_of_atoms_index + 1])

            # This will be responsible fot printing atoms names.

            info_atoms_text = ""
            for k in qtl_data_bands[0].splitlines():
                if k.startswith("JATOM"):
                    d = k.split('tot,')
                    d2 = d[1].split(',')
                    for i in d2:
                        for e in unicodes:
                            if e == i:
                                d2[d2.index(i)] = unicodes[e]
                    for i in d2:
                        d2[d2.index(i)] = i.lower()
                    d2 = ", ".join(d2)
                    info_atoms_text += str(d[0]) + " AO: tot, " + str(d2) + "<br>"

            # Gathering data for band character.

            orbitals_dict = {}

            for i in range(1, number_of_atoms + 1):
                orbitals_dict[f'JATOM {i}'] = []

            orbitals_list = []

            for e in qtl_data_heading:
                if e.startswith('tot'):
                    d = e.upper().split(',')
                    orbitals_list.append(d)

            for list in orbitals_list:
                for i in list:
                    for e in unicodes:
                        if e == i:
                            list[list.index(i)] = unicodes[e]

            for i in range(1, number_of_atoms + 1):
                orbitals_dict[f'JATOM {i}'].append(orbitals_list[i - 1])

            for i in range(20, 31):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            share_of_the_orbitals_of_atoms = {}

            # Create a dictionary, in which ATOMS are keys and also dictionaries.
            # ATOMS dictionaries contain dictionaries, whose names are the names of the orbitals of given atom,
            # and keys - bands.

            for i in range(1, number_of_atoms + 1):
                jatom_keys = orbitals_dict[f'JATOM {i}'][0]
                share_of_the_orbitals_of_atoms['JATOM ' + str(i)] = {k: {} for k in jatom_keys}
                k = f' {i} '

                for j in range(1, len(jatom_keys) + 1):
                    share_of_the_orbitals_of_atoms[f'JATOM {i}'][jatom_keys[j - 1]] = {}

                    for a in range(1, len(prepare_energy_data.keys()) + 1):
                        share_of_the_orbitals_of_atoms[f'JATOM {i}'][jatom_keys[j - 1]][f'Band {a}'] = []

                        for el in prepare_energy_data[f'Band {a}']:
                            if k in el:
                                d = el.split(k)[1]
                                kk = d.split()
                                [float(i) for i in kk]
                                share_of_the_orbitals_of_atoms[f'JATOM {i}'][jatom_keys[j - 1]][f'Band {a}'].append(
                                    float(kk[j - 1]))


            for i in range(31, 51):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            with open(spaghetti_path, 'r+') as f:
                spaghetti_data = f.read()

            # Now, data from spaghetti_ene file is extracted.
            # The only thing needed from this file is k vactor path.

            prepare_spaghetti_data = ""

            for line in spaghetti_data.splitlines():
                line = line.strip()
                prepare_spaghetti_data += (line + "\n")

            spaghetti_data_band = prepare_spaghetti_data.split('bandindex:')

            spaghetti_data_band_split = []

            energy = {}

            for e in spaghetti_data_band:
                e = e.splitlines()
                spaghetti_data_band_split.append(e)

            for i in range(1, len(spaghetti_data_band_split)):
                energy[f'Band {int(spaghetti_data_band_split[i][0])}'] = {'Energy in eV': [], 'Energy in Ry': [],
                                                                          'Energy in Ry - Fermi at 0': []}

            # Here dictionary which contains all energies (in eV, Ry, and Ry minus Fermi Energy) is created.
            # Each key (energy unit) is another dictionary, in which keys are band numbers.
            # It is used to create dataframe.

            for band in dict_all_energies:
                for i in range(1, len(dict_all_energies[band]), number_of_atoms + 1):
                    abc = float(dict_all_energies[band][i])
                    energy[band]['Energy in Ry'].append(abc)
                    energy_eV = round((abc - fermi_Energy) * 13.605684958731, 5)
                    energy[band]['Energy in eV'].append(energy_eV)
                    energy_Ry_fermi_0 = abc - fermi_Energy
                    energy[band]['Energy in Ry - Fermi at 0'].append(energy_Ry_fermi_0)

            # Finding the largest and smallest energy values for each unit.

            min_energies_in_bands_eV = []
            max_energies_in_bands_eV = []
            min_energies_in_bands_Ry = []
            max_energies_in_bands_Ry = []

            for band in energy:
                mins = min(energy[band]['Energy in eV'])
                maxs = max(energy[band]['Energy in eV'])
                min_energies_in_bands_eV.append(mins)
                max_energies_in_bands_eV.append(maxs)
                mins2 = min(energy[band]['Energy in Ry'])
                maxs2 = max(energy[band]['Energy in Ry'])
                min_energies_in_bands_Ry.append(mins2)
                max_energies_in_bands_Ry.append(maxs2)

            min_energy_in_eV = min(min_energies_in_bands_eV)
            max_energy_in_eV = max(max_energies_in_bands_eV)
            min_energy_in_Ry = min(min_energies_in_bands_Ry)
            max_energy_in_Ry = max(max_energies_in_bands_Ry)

            for i in range(50, 71):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            number_of_bands = len(energy)

            k_path = []

            # K_path must be secured against situation like: 0.0000-121.12312,
            # so k_path is taken from the middle of spaghetti_ene file.

            x = int(round(number_of_bands / 2, 0))

            for e in spaghetti_data_band_split[x]:
                try:
                    if len(e) < 7:
                        continue
                    k_vector = (e.split()[3])
                    k_path.append(float(k_vector))

                except IndexError:
                    pass

                if len(k_path) == len(energy['Band 1']['Energy in eV']):
                    break

            with open(klist_band_path, 'r+') as f:
                klist_data = f.read()

            # Now k-vector data from klist_band file is prepared.

            prepare_klist_data = ""

            for line in klist_data.splitlines():
                line = line.strip()
                prepare_klist_data += (line + "\n")

            prepare_klist_data_split = prepare_klist_data.splitlines()

            prepare_klist_data_2 = []

            for i in range(71, 81):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            for e in prepare_klist_data_split:
                e = e.splitlines()
                prepare_klist_data_2.append(e)

            prepare_klist_data_3 = []

            for e in prepare_klist_data_2:
                for i in e:
                    k = (i.split())
                    prepare_klist_data_3.append(k)

            k_vec = {'K-Vec-x': [], 'K-Vec-y': [], 'K-Vec-z': [], 'K-Vec': []}
            high_symmetry_points = []
            for e in prepare_klist_data_3:
                if len(e) > 5:
                    k_vec['K-Vec-x'].append(float(e[1]) / float(e[4]))
                    k_vec['K-Vec-y'].append(float(e[2]) / float(e[4]))
                    k_vec['K-Vec-z'].append(float(e[3]) // float(e[4]))
                    high_symmetry_points.append(e[0])
                if len(e) == 5:
                    k_vec['K-Vec-x'].append(float(e[0]) / float(e[3]))
                    k_vec['K-Vec-y'].append(float(e[1]) / float(e[3]))
                    k_vec['K-Vec-z'].append(float(e[2]) / float(e[3]))

            for i in range(80,96):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            for i in range(0, len(k_vec['K-Vec-x'])):
                e = (k_vec['K-Vec-x'][i], k_vec['K-Vec-y'][i], k_vec['K-Vec-z'][i])
                k_vec['K-Vec'].append(e)

            high_symmetry_points_indexes = []

            for e in prepare_klist_data_3:
                if len(e) > 5:
                    # Elements needs to be removed, because while there are two same high symmetry points,
                    # it returns the same indexes.
                    high_symmetry_points_indexes.append(prepare_klist_data_3.index(e))
                    e.pop()

            legend_values = []

            for i in high_symmetry_points_indexes:
                legend_values.append(k_path[i])

            for i in high_symmetry_points:
                for e in unicodes:
                    if e == i:
                        high_symmetry_points[high_symmetry_points.index(i)] = unicodes[e]

            # Creating energy dataframe, which will be used to create plots with plotly.

            energy_df = (pd.DataFrame(energy)).transpose()

            for i in range(95,101):
                time.sleep(0.05)
                self.progress_Bar.setValue(i)

            self.next_button.show()

        # Error handling, it prevents the occurrence of certain errors.

        except FileNotFoundError:
            if len(file_names[0]) == 3:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Selected data is invalid.\n'
                                     'Please make sure you have selected\n'
                                     'proper files.')
                error_dialog.exec_()
            elif len(file_names[0]) < 3:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Not all files were selected.\n'
                                     'Please select all required files.')
                error_dialog.exec_()
            pass
        except ValueError:
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Selected data is invalid.\n'
                                 'Please make sure you have selected\n'
                                 'proper files.')
            error_dialog.exec_()
            self.progress_Bar.setValue(0)
            pass
        except KeyError:
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Selected files contain invalid data.\n'
                                 'Please check your files for proper bands number.')
            error_dialog.exec_()
            self.progress_Bar.setValue(0)
            pass
        except:
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('FATAL ERROR.\n'
                                 'Unknown error occured.')
            error_dialog.exec_()
            self.progress_Bar.setValue(0)

    def next_button_clicked(self):

        # Pass data to Main Window.

        self.dialog.draw_band_structure_button.disconnect()
        self.dialog.effective_mass_button.disconnect()
        self.dialog.draw_character.disconnect()
        self.hide()
        self.dialog.show()
        self.dialog.draw_band_structure_button.clicked.connect(self.draw_band_structure)
        self.dialog.lattice_a_line.setText(str(round(lattice_a, 4)))
        self.dialog.lattice_b_line.setText(str(round(lattice_b, 4)))
        self.dialog.lattice_c_line.setText(str(round(lattice_c, 4)))
        self.dialog.compound_label.setText("<b>Compound: " + str(compound_name))
        self.dialog.label_atom_info.setText(info_atoms_text)
        self.dialog.label_atom_info.adjustSize()
        self.dialog.fermi_energy_label.setText("Fermi energy: " + str(fermi_Energy) + " [Ry]" +"  ("+ str(round(fermi_Energy*13.605684958731, 5))+ " [eV])")

        self.dialog.new_file_action.triggered.connect(self.new_file_action_clicked)
        self.dialog.close_program_action.triggered.connect(QApplication.instance().quit)

        self.dialog.minimum_energy_line.setText(str(round(min_energy_in_eV, 4)) + " [eV]")
        self.dialog.maximum_energy_line.setText(str(round(max_energy_in_eV, 4)) + " [eV]")
        self.dialog.energy_eV.clicked.connect(self.energy_in_eV_set)
        self.dialog.energy_Ry.toggled.connect(self.energy_in_Ry_set)
        self.dialog.fermi_yes_button.clicked.connect(self.energy_in_Ry_fermi_to_0_set)
        self.dialog.fermi_no_button.clicked.connect(self.energy_in_Ry_fermi_not_to_0_set)
        self.dialog.draw_character.clicked.connect(self.draw_character_with_char_marker_size)
        self.dialog.effective_mass_button.clicked.connect(self.effective_mass_button_clicked)

        # Orbitals check boxes which are used to plot band structures with band character are made.

        global check_orbital_box

        check_orbital_box = []

        for atom in share_of_the_orbitals_of_atoms:
            for e in share_of_the_orbitals_of_atoms[atom]:
                check_orbital_box.append(atom + " - " + e.lower())

        for i, v in enumerate(check_orbital_box):
            check_orbital_box[i] = QCheckBox(v)
            self.dialog.layying2.addWidget(check_orbital_box[i])
            check_orbital_box[i].setChecked(False)
            check_orbital_box[i].stateChanged.connect(self.state_changed)

        self.dialog.char_marker_size.setChecked(True)
        self.dialog.char_marker_size.clicked.connect(self.char_marker_size_button_clicked)
        self.dialog.color.clicked.connect(self.color_button_clicked)

    def energy_in_eV_set(self):
        self.dialog.minimum_energy_line.setText(str(round(min_energy_in_eV, 4)) + " [eV]")
        self.dialog.maximum_energy_line.setText(str(round(max_energy_in_eV, 4)) + " [eV]")

    def energy_in_Ry_set(self):
        self.dialog.minimum_energy_line.setText(str(round(min_energy_in_Ry, 4)) + " [Ry]")
        self.dialog.maximum_energy_line.setText(str(round(max_energy_in_Ry, 4)) + " [Ry]")

    def energy_in_Ry_fermi_to_0_set(self):
        self.dialog.minimum_energy_line.setText(str(round(min_energy_in_Ry-fermi_Energy, 4)) + " [Ry]")
        self.dialog.maximum_energy_line.setText(str(round(max_energy_in_Ry-fermi_Energy, 4)) + " [Ry]")

    def energy_in_Ry_fermi_not_to_0_set(self):
        self.dialog.minimum_energy_line.setText(str(round(min_energy_in_Ry, 4)) + " [Ry]")
        self.dialog.maximum_energy_line.setText(str(round(max_energy_in_Ry, 4)) + " [Ry]")


    def draw_band_structure(self):

        try:
            if len(self.dialog.highest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    max_range = max_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_range = max_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_range = max_energy_in_Ry - fermi_Energy

            else:
                max_range = float(self.dialog.highest_input_line.text().replace(',', '.'))

            if len(self.dialog.lowest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    min_range = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    min_range = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    min_range = min_energy_in_Ry - fermi_Energy
            else:
                min_range = float(self.dialog.lowest_input_line.text().replace(',', '.'))

        except(ValueError):
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Energy range needs to be numerical value.\n'
                                 'Please correct the input energy range.')
            error_dialog.exec_()

        fig = go.Figure()

        if self.dialog.energy_eV.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                         text=k_vec['K-Vec'], mode='lines', line=dict(color="cornflowerblue"),
                                         name=f'Band {band + 1}',
                                         hovertemplate="Energy: %{y:.4f} [Ev] <br>k-vec%{text}"))
                fig.update_yaxes(title_text='E-Ef [eV]')

        elif self.dialog.fermi_no_button.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                         text=k_vec['K-Vec'], mode='lines', line=dict(color="cornflowerblue"),
                                         name=f'Band {band + 1}',
                                         hovertemplate="Energy: %{y:.4f} [Ry] <br>k-vec%{text}"))
            fig.update_yaxes(title_text='E [Ry]')

        elif self.dialog.fermi_yes_button.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                         text=k_vec['K-Vec'], mode='lines', line=dict(color="cornflowerblue"),
                                         name=f'Band {band + 1}',
                                         hovertemplate="Energy: %{y:.4f} [Ry] <br>k-vec%{text}"))
            fig.update_yaxes(title_text='E-Ef [Ry]')

        fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True, showline=True,
                         linecolor="DimGrey", range=[0, k_path[-1]])

        try:
            fig.update_yaxes(showgrid=False, mirror=True, showline=True, linecolor="DimGrey",
                             ticks="outside", range=[min_range, max_range])
        except(UnboundLocalError):
            pass

        fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                          modebar_activecolor="DarksLateGray")

        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            args=[{'line.color': "cornflowerblue"}],
                            label="cornflowerblue",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "mediumseagreen"}],
                            label="mediumseagreen",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "darkslategray"}],
                            label="darkslategray",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "darkgoldenrod"}],
                            label="darkgoldenrod",
                            method="restyle"
                        ),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.1,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=[{'plot_bgcolor': "white"}],
                            label="white",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "ivory"}],
                            label="ivory",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "whitesmoke"}],
                            label="whitesmoke",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "snow"}],
                            label="snow",
                            method="relayout"
                        ),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.40,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=[{"line.width": 2}],
                            label="2",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 1}],
                            label="1",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 1.5}],
                            label="1.5",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 2.5}],
                            label="2.5",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 3}],
                            label="3",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 3.5}],
                            label="3.5",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.65,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=["showlegend", True],
                            label="True",
                            method="restyle"
                        ),
                        dict(
                            args=["showlegend", False],
                            label="False",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.88,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                )
            ]

        )
        fig.update_layout(
            annotations=[
                dict(text="Line<br>color:", x=0.02, xref="paper", y=1.09, yref="paper",
                     align="left", showarrow=False),
                dict(text="Background<br>color:", x=0.30, xref="paper", y=1.10,
                     yref="paper", showarrow=False),
                dict(text="Line<br>width:", x=0.61, xref="paper", y=1.10, yref="paper",
                     showarrow=False),
                dict(text="Show<br>legend:", x=0.82, xref="paper", y=1.10, yref="paper",
                     showarrow=False)
            ])

        if self.dialog.energy_eV.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

        elif self.dialog.fermi_yes_button.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

        elif self.dialog.fermi_no_button.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")


        fig.update_layout(
            font_family="Tahoma",
            font_color="dimgrey"
        )

        for i in range(0, len(legend_values)):
            fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                          annotation_text=high_symmetry_points[i],
                          annotation_position="bottom")

        config = {
            'toImageButtonOptions': {
                'filename': compound_name,
                'height': 700,
                'width': 900,
                'scale': 3
            }
        }

        try:
            if self.dialog.energy_eV.isChecked():
                max_available_energy = max_energy_in_eV
                min_available_energy = min_energy_in_eV
            elif self.dialog.fermi_no_button.isChecked():
                max_available_energy = max_energy_in_Ry
                min_available_energy = min_energy_in_Ry
            elif self.dialog.fermi_yes_button.isChecked():
                max_available_energy = max_energy_in_Ry - fermi_Energy
                min_available_energy = min_energy_in_Ry - fermi_Energy

            if max_range > max_available_energy:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Your max range is higher than max available energy.\n'
                                     'Please correct the input energy range.')
                error_dialog.exec_()
            elif min_range < min_available_energy:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Your min range is lower than min available energy.\n'
                                     'Please correct the input energy range.')
                error_dialog.exec_()
            elif max_range > min_range:
                fig.show(config=config)
            else:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                         'Please correct the input energy range.')
                error_dialog.exec_()
        except(UnboundLocalError):
            pass

    def new_file_action_clicked(self):
        self.show()
        self.dialog.close()
        self.next_button.hide()
        self.progress_Bar.setValue(0)

        for i, v in enumerate(check_orbital_box):
            check_orbital_box[i].deleteLater()


    def effective_mass_button_clicked(self):

        def find_coefficients(np_index, x_array, y_array):

            try:
                # Quadratic interpolation on the basis of ten points closest to a given extreme.
                new_indices = np.array(
                    [np_index - 5, np_index - 4, np_index - 3, np_index - 2, np_index - 1, np_index, np_index + 1,
                     np_index + 2, np_index + 3, np_index + 4, np_index + 5])
                x_interpolate = (1 / 5.29177210671212 * (10 ** 11)) * x_array[new_indices]
                y_interpolate = (1.602 * (10 ** -19)) * y_array[new_indices]
                c1 = np.polyfit(x_interpolate, y_interpolate, 2)
                return c1[0]

            except:
                # If the extreme is close to the end of band structure plot, it not always have five points
                # with lower/higher indexes. So quadratic interpolation needs to be carried out on
                # the basis of two closest points and the given extreme.
                new_indices = np.array([np_index - 1, np_index, np_index + 1, ])
                x_interpolate = (1 / 5.29177210671212 * (10 ** 11)) * x_array[new_indices]
                y_interpolate = (1.602 * (10 ** -19)) * y_array[new_indices]
                c1 = np.polyfit(x_interpolate, y_interpolate, 2)
                return c1[0]

        try:
            if len(self.dialog.highest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    max_range = max_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_range = max_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_range = max_energy_in_Ry - fermi_Energy

            else:
                max_range = float(self.dialog.highest_input_line.text().replace(',', '.'))

            if len(self.dialog.lowest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    min_range = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    min_range = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    min_range = min_energy_in_Ry - fermi_Energy
            else:
                min_range = float(self.dialog.lowest_input_line.text().replace(',', '.'))

        except(ValueError):
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Energy range needs to be numerical value.\n'
                                 'Please correct the input energy range.')
            error_dialog.exec_()

        # Effective mass is a dictionary, that will be added to energy data frame. Marker effectiver mass size is
        # a dictionary that will be responsible for adding points (size 20), where local extreme is found.

        effective_mass = {}
        marker_effective_mass_size = {}

        for band in range(1, len(energy_df.index) + 1):
            effective_mass[f'Band {band}'] = {'Effective mass': []}
            marker_effective_mass_size[f'Band {band}'] = []

        for band in energy:
            for e in range(0, len(k_path)):
                effective_mass[band]['Effective mass'].append('-')
                marker_effective_mass_size[band].append(0)

        # Looking for local extremes.

        for band in energy:
            x2 = np.array(k_path)
            y2 = np.array(energy[band]['Energy in eV'])

            minimums = argrelextrema(y2, np.less)
            maximums = argrelextrema(y2, np.greater)

            for e in minimums:
                for i in e:
                    element = find_coefficients(i, x2, y2)
                    mass = str(round((1.05 * 10 ** (-34)) ** 2 / element / (9.11 * 10 ** (-31)), 4)) + "me"
                    effective_mass[band]['Effective mass'][i] = mass
                    marker_effective_mass_size[band][i] = 10

            for e in maximums:
                for i in e:
                    element = find_coefficients(i, x2, y2)
                    mass = str(round((1.05 * 10 ** (-34)) ** 2 / element / (9.11 * 10 ** (-31)), 4)) + "me"
                    effective_mass[band]['Effective mass'][i] = mass
                    marker_effective_mass_size[band][i] = 10

        energy_df['Effective mass'] = (pd.DataFrame(effective_mass)).transpose()

        fig = go.Figure()

        if self.dialog.energy_eV.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(
                    go.Scatter(x=k_path, y=energy_df['Energy in eV'][band], hovertext=energy_df['Effective mass'][band],
                               text=k_vec['K-Vec'], mode='markers+lines', line=dict(color="cornflowerblue"),
                               marker=dict(size=[element for element in marker_effective_mass_size[f'Band {1 + band}']],
                                           opacity=0.4, color="darkcyan"),
                               name=f'Band {band + 1}',
                               hovertemplate="Effective mass: %{hovertext} <br>Energy: %{y:.4f} [Ev] <br>k-vec%{text}"))
            fig.update_yaxes(title_text='E-Ef [eV]')

        elif self.dialog.fermi_no_button.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(
                    go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band], hovertext=energy_df['Effective mass'][band],
                               text=k_vec['K-Vec'], mode='markers+lines', line=dict(color="cornflowerblue"),
                               marker=dict(size=[element for element in marker_effective_mass_size[f'Band {1 + band}']],
                                           opacity=0.4, color="darkcyan"),
                               name=f'Band {band + 1}',
                               hovertemplate="Effective mass: %{hovertext} <br>Energy: %{y:.4f} [Ev] <br>k-vec%{text}"))

            fig.update_yaxes(title_text='E [Ry]')

        elif self.dialog.fermi_yes_button.isChecked():

            for band in range(0, len(energy_df.index)):
                fig.add_trace(
                    go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band], hovertext=energy_df['Effective mass'][band],
                               text=k_vec['K-Vec'], mode='markers+lines', line=dict(color="cornflowerblue"),
                               marker=dict(size=[element for element in marker_effective_mass_size[f'Band {1 + band}']],
                                           opacity=0.4, color="darkcyan"),
                               name=f'Band {band + 1}',
                               hovertemplate="Effective mass: %{hovertext} <br>Energy: %{y:.4f} [Ev] <br>k-vec%{text}"))

            fig.update_yaxes(title_text='E-Ef [Ry]')

        fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True, showline=True,
                         linecolor="DimGrey", range=[0, k_path[-1]])

        try:
            fig.update_yaxes(title_text='E-Ef [eV]', showgrid=False, mirror=True, showline=True, linecolor="DimGrey",
                             ticks="outside", range=[min_range, max_range])
        except(UnboundLocalError):
            pass

        fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                          modebar_activecolor="DarksLateGray")

        fig.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            args=[{'line.color': "cornflowerblue"}],
                            label="cornflowerblue",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "mediumseagreen"}],
                            label="mediumseagreen",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "darkslategray"}],
                            label="darkslategray",
                            method="restyle"
                        ),
                        dict(
                            args=[{'line.color': "darkgoldenrod"}],
                            label="darkgoldenrod",
                            method="restyle"
                        ),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.07,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=[{'marker.color': "darkcyan"}],
                            label="darkcyan",
                            method="restyle"
                        ),
                        dict(
                            args=[{'marker.color': "forestgreen"}],
                            label="forestgreen",
                            method="restyle"
                        ),
                        dict(
                            args=[{'marker.color': "black"}],
                            label="black",
                            method="restyle"
                        ),
                        dict(
                            args=[{'marker.color': "saddlebrown"}],
                            label="saddlebrown",
                            method="restyle"
                        ),
                        dict(
                            args=[{'marker.color': "purple"}],
                            label="purple",
                            method="restyle"
                        ),
                        dict(
                            args=[{'marker.color': "maroon"}],
                            label="maroon",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.30,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=[{'plot_bgcolor': "white"}],
                            label="white",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "ivory"}],
                            label="ivory",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "whitesmoke"}],
                            label="whitesmoke",
                            method="relayout"
                        ),
                        dict(
                            args=[{'plot_bgcolor': "snow"}],
                            label="snow",
                            method="relayout"
                        ),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.54,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=[{"line.width": 2}],
                            label="2",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 1}],
                            label="1",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 1.5}],
                            label="1.5",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 2.5}],
                            label="2.5",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 3}],
                            label="3",
                            method="restyle"
                        ),
                        dict(
                            args=[{"line.width": 3.5}],
                            label="3.5",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.74,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            args=["showlegend", True],
                            label="True",
                            method="restyle"
                        ),
                        dict(
                            args=["showlegend", False],
                            label="False",
                            method="restyle"
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.91,
                    xanchor="left",
                    y=1.12,
                    yanchor="top"
                )
            ]

        )
        fig.update_layout(
            annotations=[
                dict(text="Line<br>color:", x=0.01, xref="paper", y=1.10, yref="paper",
                     align="left", showarrow=False),
                dict(text="Marker<br>color:", x=0.24, xref="paper", y=1.10,
                     yref="paper", showarrow=False),
                dict(text="Background<br>color:", x=0.48, xref="paper", y=1.10,
                     yref="paper", showarrow=False),
                dict(text="Line<br>width:", x=0.73, xref="paper", y=1.10, yref="paper",
                     showarrow=False),
                dict(text="Show<br>legend:", x=0.88, xref="paper", y=1.10, yref="paper",
                     showarrow=False)
            ])

        if self.dialog.energy_eV.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

        elif self.dialog.fermi_yes_button.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

        elif self.dialog.fermi_no_button.isChecked():
            fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                          line=dict(color="rosybrown", dash="dash"), name="Fermi energy")


        fig.update_layout(
            font_family="Tahoma",
            font_color="dimgrey"
        )

        for i in range(0, len(legend_values)):
            fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                          annotation_text=high_symmetry_points[i],
                          annotation_position="bottom")
        config = {
            'toImageButtonOptions': {
                'filename': compound_name,
                'height': 750,
                'width': 1000,
                'scale': 3
            }
        }
        try:
            if self.dialog.energy_eV.isChecked():
                max_available_energy = max_energy_in_eV
                min_available_energy = min_energy_in_eV
            elif self.dialog.fermi_no_button.isChecked():
                max_available_energy = max_energy_in_Ry
                min_available_energy = min_energy_in_Ry
            elif self.dialog.fermi_yes_button.isChecked():
                max_available_energy = max_energy_in_Ry - fermi_Energy
                min_available_energy = min_energy_in_Ry - fermi_Energy

            if max_range > max_available_energy:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Your max range is higher than max available energy.\n'
                                     'Please correct the input energy range.')
                error_dialog.exec_()
            elif min_range < min_available_energy:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Your min range is lower than min available energy.\n'
                                     'Please correct the input energy range.')
                error_dialog.exec_()
            elif max_range > min_range:
                fig.show(config=config)
            else:
                error_dialog = QMessageBox()
                error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setWindowTitle("Error Message")
                error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                     'Please correct the input energy range.')
                error_dialog.exec_()
        except(UnboundLocalError):
            pass

    def char_marker_size_button_clicked(self):
        for i, v in enumerate(check_orbital_box):
            check_orbital_box[i].setChecked(False)

        self.dialog.draw_character.disconnect()
        self.dialog.draw_character.clicked.connect(self.draw_character_with_char_marker_size)

    def color_button_clicked(self):
        for i, v in enumerate(check_orbital_box):
            check_orbital_box[i].setChecked(False)
        self.dialog.draw_character.disconnect()
        self.dialog.draw_character.clicked.connect(self.draw_character_with_color)

    def state_changed(self, state):
        if self.dialog.char_marker_size.isChecked():
            # It prevents from checking more than one box.
            for i, v in enumerate(check_orbital_box):
                if state == QtCore.Qt.Checked:
                    if self.sender() == check_orbital_box[i]:
                        for l, m in enumerate(check_orbital_box):
                            if l != i:
                                check_orbital_box[l].setChecked(False)
        elif self.dialog.color.isChecked():
            # It allows to check up to 3 boxes.
            k = 0
            for i, v in enumerate(check_orbital_box):
                if check_orbital_box[i].isChecked():
                    k += 1
                    if k > 3:
                        for l, m in enumerate(check_orbital_box):
                            check_orbital_box[l].setChecked(False)
                            k = 0

    def draw_character_with_char_marker_size(self):

        # Multiplier by which share of checked orbital will be multiplied.

        multiplier = 3

        if self.dialog.three_button.isChecked():
            multiplier = 3

        elif self.dialog.five_button.isChecked():
            multiplier = 5

        elif self.dialog.ten_button.isChecked():
            multiplier = 10

        elif self.dialog.fifteen_button.isChecked():
            multiplier = 15

        for i, v in enumerate(check_orbital_box):

            if check_orbital_box[i].isChecked():
                key1 = check_orbital_box[i].text().split()[0] + " " + check_orbital_box[i].text().split()[1]
                key2 = check_orbital_box[i].text().split()[3].upper()

                orb_name = check_orbital_box[i].text()

                try:
                    if len(self.dialog.highest_input_line.text()) == 0:
                        if self.dialog.energy_eV.isChecked():
                            max_range = max_energy_in_eV
                        elif self.dialog.fermi_no_button.isChecked():
                            max_range = max_energy_in_Ry
                        elif self.dialog.fermi_yes_button.isChecked():
                            max_range = max_energy_in_Ry - fermi_Energy

                    else:
                        max_range = float(self.dialog.highest_input_line.text().replace(',', '.'))

                    if len(self.dialog.lowest_input_line.text()) == 0:
                        if self.dialog.energy_eV.isChecked():
                            min_range = min_energy_in_eV
                        elif self.dialog.fermi_no_button.isChecked():
                            min_range = min_energy_in_Ry
                        elif self.dialog.fermi_yes_button.isChecked():
                            min_range = min_energy_in_Ry - fermi_Energy
                    else:
                        min_range = float(self.dialog.lowest_input_line.text().replace(',', '.'))

                except(ValueError):
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Energy range needs to be numerical value.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()

                marker_size = share_of_the_orbitals_of_atoms[key1][key2]
                fig = go.Figure()

                if self.dialog.energy_eV.isChecked():

                    for band in range(0, len(energy_df.index)):
                        fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                                 text=k_vec['K-Vec'], mode='markers+lines',
                                                 marker=dict(color='cornflowerblue',
                                                             size=[element * multiplier for element in
                                                                   marker_size[f'Band {1 + band}']],
                                                             line=dict(color='cornflowerblue', width=2)),
                                                 name=f'Band {band + 1}',
                                                 hovertext=marker_size[f'Band {1 + band}'],
                                                 hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + orb_name + ": %{hovertext}"))
                    fig.update_yaxes(title_text='E-Ef [eV]')

                elif self.dialog.fermi_no_button.isChecked():

                    for band in range(0, len(energy_df.index)):
                        fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                                 text=k_vec['K-Vec'], mode='markers+lines',
                                                 marker=dict(color='cornflowerblue',
                                                             size=[element * multiplier for element in
                                                                   marker_size[f'Band {1 + band}']],
                                                             line=dict(color='cornflowerblue', width=2)),
                                                 name=f'Band {band + 1}',
                                                 hovertext=marker_size[f'Band {1 + band}'],
                                                 hovertemplate="Energy: %{y:.4f} [Ry] <br>k-vec%{text} <br>Orbital share:<br>" + orb_name + ": % %{hovertext}"))

                    fig.update_yaxes(title_text='E [Ry]')

                elif self.dialog.fermi_yes_button.isChecked():

                    for band in range(0, len(energy_df.index)):
                        fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                                 text=k_vec['K-Vec'], mode='markers+lines',
                                                 marker=dict(color='cornflowerblue',
                                                             size=[element * multiplier for element in
                                                                   marker_size[f'Band {1 + band}']],
                                                             line=dict(color='cornflowerblue', width=2)),
                                                 name=f'Band {band + 1}',
                                                 hovertext=marker_size[f'Band {1 + band}'],
                                                 hovertemplate="Energy: %{y:.4f} [Ry] <br>k-vec%{text} <br>Orbital share:<br>" + orb_name + ": % %{hovertext}"))

                    fig.update_yaxes(title_text='E-Ef [Ry]')

                fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True,
                                         showline=True,
                                         linecolor="DimGrey", range=[0, k_path[-1]])

                try:
                    fig.update_yaxes(title_text='E-Ef [eV]', showgrid=False, mirror=True, showline=True,
                                     linecolor="DimGrey",
                                     ticks="outside", range=[min_range, max_range])
                except(UnboundLocalError):
                    pass

                fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                                  modebar_activecolor="DarksLateGray")

                fig.update_layout(
                    updatemenus=[
                        dict(
                            buttons=list([
                                dict(
                                    args=[{'line.color': "cornflowerblue"}],
                                    label="cornflowerblue",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'line.color': "mediumseagreen"}],
                                    label="mediumseagreen",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'line.color': "darkslategray"}],
                                    label="darkslategray",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'line.color': "darkgoldenrod"}],
                                    label="darkgoldenrod",
                                    method="restyle"
                                ),
                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0.06,
                            xanchor="left",
                            y=1.12,
                            yanchor="top"
                        ),
                        dict(
                            buttons=list([
                                dict(
                                    args=[{'plot_bgcolor': "white"}],
                                    label="white",
                                    method="relayout"
                                ),
                                dict(
                                    args=[{'plot_bgcolor': "ivory"}],
                                    label="ivory",
                                    method="relayout"
                                ),
                                dict(
                                    args=[{'plot_bgcolor': "whitesmoke"}],
                                    label="whitesmoke",
                                    method="relayout"
                                ),
                                dict(
                                    args=[{'plot_bgcolor': "snow"}],
                                    label="snow",
                                    method="relayout"
                                ),
                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0.31,
                            xanchor="left",
                            y=1.12,
                            yanchor="top"
                        ),
                        dict(
                            buttons=list([
                                dict(
                                    args=[{'marker.color': "royalblue"}],
                                    label="royalblue",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.color': "seagreen"}],
                                    label="seagreen",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.color': "black"}],
                                    label="black",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.color': "saddlebrown"}],
                                    label="saddlebrown",
                                    method="restyle"
                                ),
                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0.50,
                            xanchor="left",
                            y=1.12,
                            yanchor="top"
                        ),
                        dict(
                            buttons=list([
                                dict(
                                    args=[{'marker.line.color': "royalblue"}],
                                    label="royalblue",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.line.color': "seagreen"}],
                                    label="seagreen",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.line.color': "black"}],
                                    label="black",
                                    method="restyle"
                                ),
                                dict(
                                    args=[{'marker.line.color': "saddlebrown"}],
                                    label="saddlebrown",
                                    method="restyle"
                                ),
                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0.72,
                            xanchor="left",
                            y=1.12,
                            yanchor="top"
                        ),
                        dict(
                            buttons=list([
                                dict(
                                    args=["showlegend", True],
                                    label="True",
                                    method="restyle"
                                ),
                                dict(
                                    args=["showlegend", False],
                                    label="False",
                                    method="restyle"
                                )
                            ]),
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                            x=0.93,
                            xanchor="left",
                            y=1.12,
                            yanchor="top"
                        )
                    ]

                )
                fig.update_layout(
                    annotations=[
                        dict(text="Line<br>color:", x=0.01, xref="paper", y=1.09, yref="paper",
                             align="left", showarrow=False),
                        dict(text="Background<br>color:", x=0.23, xref="paper", y=1.10,
                             yref="paper", showarrow=False),
                        dict(text="Marker<br>color:", x=0.47, xref="paper", y=1.10,
                             yref="paper", showarrow=False),
                        dict(text="Marker line<br>color:", x=0.715, xref="paper", y=1.10,
                             yref="paper", showarrow=False),
                        dict(text="Show<br>legend:", x=0.91, xref="paper", y=1.10, yref="paper",
                             showarrow=False)
                    ])

                if self.dialog.energy_eV.isChecked():
                    fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                                  line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

                elif self.dialog.fermi_yes_button.isChecked():
                    fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                                  line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

                elif self.dialog.fermi_no_button.isChecked():
                    fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                                  line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

                fig.update_layout(
                    font_family="Tahoma",
                    font_color="dimgrey"
                )

                for i in range(0, len(legend_values)):
                    fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                                  annotation_text=high_symmetry_points[i],
                                  annotation_position="bottom")

                config = {
                    'toImageButtonOptions': {
                        'filename': compound_name,
                        'height': 750,
                        'width': 1000,
                        'scale': 3
                    }
                }

                try:
                    if self.dialog.energy_eV.isChecked():
                        max_available_energy = max_energy_in_eV
                        min_available_energy = min_energy_in_eV
                    elif self.dialog.fermi_no_button.isChecked():
                        max_available_energy = max_energy_in_Ry
                        min_available_energy = min_energy_in_Ry
                    elif self.dialog.fermi_yes_button.isChecked():
                        max_available_energy = max_energy_in_Ry - fermi_Energy
                        min_available_energy = min_energy_in_Ry - fermi_Energy

                    if max_range > max_available_energy:
                        error_dialog = QMessageBox()
                        error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                        error_dialog.setIcon(QMessageBox.Warning)
                        error_dialog.setWindowTitle("Error Message")
                        error_dialog.setText('Your max range is higher than max available energy.\n'
                                             'Please correct the input energy range.')
                        error_dialog.exec_()
                    elif min_range < min_available_energy:
                        error_dialog = QMessageBox()
                        error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                        error_dialog.setIcon(QMessageBox.Warning)
                        error_dialog.setWindowTitle("Error Message")
                        error_dialog.setText('Your min range is lower than min available energy.\n'
                                             'Please correct the input energy range.')
                        error_dialog.exec_()
                    elif max_range > min_range:
                        fig.show(config=config)
                    else:
                        error_dialog = QMessageBox()
                        error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                        error_dialog.setIcon(QMessageBox.Warning)
                        error_dialog.setWindowTitle("Error Message")
                        error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                             'Please correct the input energy range.')
                        error_dialog.exec_()
                except(UnboundLocalError):
                    pass

                fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                                          modebar_activecolor="DarksLateGray")


    def draw_character_with_color(self):

        try:

            if len(self.dialog.highest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    max_range = max_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_range = max_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_range = max_energy_in_Ry - fermi_Energy

            else:
                max_range = float(self.dialog.highest_input_line.text().replace(',', '.'))

            if len(self.dialog.lowest_input_line.text()) == 0:
                if self.dialog.energy_eV.isChecked():
                    min_range = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    min_range = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    min_range = min_energy_in_Ry - fermi_Energy
            else:
                min_range = float(self.dialog.lowest_input_line.text().replace(',', '.'))

        except(ValueError):
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle("Error Message")
            error_dialog.setText('Energy range needs to be numerical value.\n'
                                 'Please correct the input energy range.')
            error_dialog.exec_()

        k = 0

        for i, v in enumerate(check_orbital_box):

            if check_orbital_box[i].isChecked():
                k += 1

        fig = go.Figure()

        # When one orbital box is checked:

        if k == 1:

            new_colorscale = {}

            for i, v in enumerate(check_orbital_box):
                if check_orbital_box[i].isChecked():
                    key1 = check_orbital_box[i].text().split()[0] + " " + check_orbital_box[i].text().split()[1]
                    key2 = check_orbital_box[i].text().split()[3].upper()

                    marker_size = share_of_the_orbitals_of_atoms[key1][key2]
                    name_orb = check_orbital_box[i].text()

                    for band in range(1, len(energy_df.index)+1):
                        new_colorscale[f'Band {band}'] = {'Color scale': []}

                    for band in new_colorscale:
                        for element in marker_size[band]:
                            new_colorscale[band]['Color scale'].append(element)

            max_orbital_share = max(marker_size.values())
            max_orbital_share = max(max_orbital_share)

            energy_df['Colorscale'] = (pd.DataFrame(new_colorscale)).transpose()

            if self.dialog.energy_eV.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share, color=energy_df['Colorscale'][band],
                                                         colorscale=[(0,'black'), (1, 'green')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share, color=energy_df['Colorscale'][band],
                                                         colorscale=[(0,'black'), (1, 'blue')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share,
                                                         color=energy_df['Colorscale'][band],
                                                         colorscale=[(0, 'black'), (1, 'red')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))

                    fig.update_yaxes(title_text='E-Ef [eV]')

            elif self.dialog.fermi_no_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share, color=energy_df['Colorscale'][band],
                                                         colorscale=[(0,'black'), (1, 'green')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share,
                                                         color=energy_df['Colorscale'][band],
                                                         colorscale=[(0, 'black'), (1, 'blue')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share,
                                                         color=energy_df['Colorscale'][band],
                                                         colorscale=[(0, 'black'), (1, 'red')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))

                    fig.update_yaxes(title_text='E [Ry]')

            elif self.dialog.fermi_yes_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share, color=energy_df['Colorscale'][band],
                                                         colorscale=[(0,'black'), (1, 'green')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share,
                                                         color=energy_df['Colorscale'][band],
                                                         colorscale=[(0, 'black'), (1, 'blue')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(cmin=0, cmax=max_orbital_share,
                                                         color=energy_df['Colorscale'][band],
                                                         colorscale=[(0, 'black'), (1, 'red')], showscale=True),
                                             name=f'Band {band + 1}',
                                             hovertext=marker_size[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>Orbital share:<br>" + name_orb + ": %{hovertext}"))

                    fig.update_yaxes(title_text='E-Ef [Ry]')

            fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                              modebar_activecolor="DarksLateGray")

            fig.update_layout(
                updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                args=[{'mode': "markers"}],
                                label="markers",
                                method="restyle"
                            ),
                            dict(
                                args=[{'mode': "markers+lines", 'line.color': "black", 'line.width': "1.5"}],
                                label="markers+lines",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.08,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'visible': [False, False, True]}],
                                label="black-red",
                                method="restyle"
                            ),
                            dict(
                                args=[{'visible': [True, False, False]}],
                                label="black-green",
                                method="restyle"
                            ),
                            dict(
                                args=[{'visible': [False, True, False]}],
                                label="black-blue",
                                method="restyle"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.35,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'marker.cmax': max_orbital_share}],
                                label="max",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.cmax': 1}],
                                label="1",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.6,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'plot_bgcolor': "white"}],
                                label="white",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "ivory"}],
                                label="ivory",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "whitesmoke"}],
                                label="whitesmoke",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "snow"}],
                                label="snow",
                                method="relayout"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.85,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    )
                ]

            )

            fig.update_layout(
                annotations=[
                    dict(text="Mode:", x=0.02, xref="paper", y=1.09, yref="paper",
                         align="left", showarrow=False),
                    dict(text="Colorscale:", x=0.25, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Cmax:", x=0.52, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Background<br>color:", x=0.8, xref="paper", y=1.10,
                         yref="paper", showarrow=False)
                ])

            fig.update_layout(showlegend=False)

            fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True,
                             showline=True,
                             linecolor="DimGrey", range=[0, k_path[-1]])

            try:
                fig.update_yaxes(title_text='E-Ef [eV]', showgrid=False, mirror=True, showline=True,
                                 linecolor="DimGrey",
                                 ticks="outside", range=[min_range, max_range])
            except(UnboundLocalError):
                pass

            if self.dialog.energy_eV.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_yes_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_no_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            fig.update_layout(
                font_family="Tahoma",
                font_color="dimgrey"
            )

            for i in range(0, len(legend_values)):
                fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                              annotation_text=high_symmetry_points[i],
                              annotation_position="bottom")

            config = {
                'toImageButtonOptions': {
                    'filename': compound_name,
                    'height': 700,
                    'width': 900,
                    'scale': 3
                }
            }

            try:
                if self.dialog.energy_eV.isChecked():
                    max_available_energy = max_energy_in_eV
                    min_available_energy = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_available_energy = max_energy_in_Ry
                    min_available_energy = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_available_energy = max_energy_in_Ry - fermi_Energy
                    min_available_energy = min_energy_in_Ry - fermi_Energy

                if max_range > max_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your max range is higher than max available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif min_range < min_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your min range is lower than min available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif max_range > min_range:
                    fig.show(config=config)
                else:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
            except(UnboundLocalError):
                pass

        # When two orbital boxes are checked:

        elif k == 2:

            new_colorscale = {}
            AO_share = {}

            for band in range(1, len(energy_df.index) + 1):
                new_colorscale[f'Band {band}'] = {'Color scale': []}

            for band in range(1, len(energy_df.index) + 1):
                AO_share[f'Band {band}'] = []

            b = 0

            for i, v in enumerate(check_orbital_box):
                if check_orbital_box[i].isChecked():
                    b = b+1
                    key1 = check_orbital_box[i].text().split()[0] + " " + check_orbital_box[i].text().split()[1]
                    key2 = check_orbital_box[i].text().split()[3].upper()

                    if b == 1:
                        marker_size_a = share_of_the_orbitals_of_atoms[key1][key2]
                        name_orb_a = check_orbital_box[i].text()
                        max_orbital_share_a = max(marker_size_a.values())
                        max_orbital_share_a = max(max_orbital_share_a)

                    if b == 2:
                        marker_size_b = share_of_the_orbitals_of_atoms[key1][key2]
                        name_orb_b = check_orbital_box[i].text()
                        max_orbital_share_b = max(marker_size_b.values())
                        max_orbital_share_b = max(max_orbital_share_b)

            for (band, a_list), (band, b_list) in zip(marker_size_a.items(), marker_size_b.items()):
                for a, b in zip(a_list, b_list):
                    color_tuple = (int(a / max_orbital_share_a * 255), int(b / max_orbital_share_b * 255), 0)
                    color_tuple = pc.label_rgb(color_tuple)
                    text = "Orbitals share:<br>" + name_orb_a + ": " + str(a) + ",<br>" + name_orb_b + ": " + str(b)
                    AO_share[band].append(text)
                    new_colorscale[band]['Color scale'].append(color_tuple)

            energy_df['Colorscale'] = (pd.DataFrame(new_colorscale)).transpose()

            if self.dialog.energy_eV.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}',
                                             hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))

                fig.update_yaxes(title_text='E-Ef [eV]')

            elif self.dialog.fermi_no_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}',
                                             hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))

                fig.update_yaxes(title_text='E [Ry]')

            elif self.dialog.fermi_yes_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry - Fermi at 0'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}',
                                             hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))

                fig.update_yaxes(title_text='E-Ef [Ry]')

            fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                              modebar_activecolor="DarksLateGray")

            fig.update_layout(
                updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                args=[{'mode': "markers"}],
                                label="markers",
                                method="restyle"
                            ),
                            dict(
                                args=[{'mode': "markers+lines", 'line.color': "black", 'line.width': "1.5"}],
                                label="markers+lines",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.08,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'plot_bgcolor': "white"}],
                                label="white",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "ivory"}],
                                label="ivory",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "whitesmoke"}],
                                label="whitesmoke",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "snow"}],
                                label="snow",
                                method="relayout"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.37,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'marker.size': 6}],
                                label="6",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 4}],
                                label="4",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 5}],
                                label="5",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 7}],
                                label="7",
                                method="restyle"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.64,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=["showlegend", True],
                                label="True",
                                method="restyle"
                            ),
                            dict(
                                args=["showlegend", False],
                                label="False",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.85,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    )
                ]

            )
            fig.update_layout(
                annotations=[
                    dict(text="Mode:", x=0.02, xref="paper", y=1.09, yref="paper",
                         align="left", showarrow=False),
                    dict(text="Background<br>color:", x=0.27, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Marker<br>size:", x=0.57, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Show<br>legend:", x=0.8, xref="paper", y=1.10, yref="paper",
                         showarrow=False)
                ])
            fig.add_annotation(
                text=f'\U0001F534 - {name_orb_a}<br>\U0001F7E2 - {name_orb_b}',
                align='left',
                showarrow=False,
                xref='paper',
                yref='paper',
                x=1,
                y=0,
                bordercolor='dimgrey',
                borderwidth=1,
                bgcolor="white"
            )

            fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True,
                             showline=True,
                             linecolor="DimGrey", range=[0, k_path[-1]])

            try:
                fig.update_yaxes(title_text='E-Ef [eV]', showgrid=False, mirror=True, showline=True,
                                 linecolor="DimGrey",
                                 ticks="outside", range=[min_range, max_range])
            except(UnboundLocalError):
                pass

            if self.dialog.energy_eV.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_yes_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_no_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            fig.update_layout(
                font_family="Tahoma",
                font_color="dimgrey"
            )

            for i in range(0, len(legend_values)):
                fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                              annotation_text=high_symmetry_points[i],
                              annotation_position="bottom")

            config = {
                'toImageButtonOptions': {
                    'filename': compound_name,
                    'height': 700,
                    'width': 900,
                    'scale': 3
                }
            }

            try:
                if self.dialog.energy_eV.isChecked():
                    max_available_energy = max_energy_in_eV
                    min_available_energy = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_available_energy = max_energy_in_Ry
                    min_available_energy = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_available_energy = max_energy_in_Ry - fermi_Energy
                    min_available_energy = min_energy_in_Ry - fermi_Energy

                if max_range > max_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your max range is higher than max available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif min_range < min_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your min range is lower than min available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif max_range > min_range:
                    fig.show(config=config)
                else:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
            except(UnboundLocalError):
                pass

        # When three orbital boxes are checked:

        elif k == 3:

            new_colorscale = {}
            AO_share = {}

            for band in range(1, len(energy_df.index) + 1):
                new_colorscale[f'Band {band}'] = {'Color scale': []}

            for band in range(1, len(energy_df.index) + 1):
                AO_share[f'Band {band}'] = []

            b = 0

            for i, v in enumerate(check_orbital_box):
                if check_orbital_box[i].isChecked():
                    b = b + 1
                    key1 = check_orbital_box[i].text().split()[0] + " " + check_orbital_box[i].text().split()[1]
                    key2 = check_orbital_box[i].text().split()[3].upper()

                    if b == 1:
                        marker_size_a = share_of_the_orbitals_of_atoms[key1][key2]
                        name_orb_a = check_orbital_box[i].text()
                        max_orbital_share_a = max(marker_size_a.values())
                        max_orbital_share_a = max(max_orbital_share_a)

                    if b == 2:
                        marker_size_b = share_of_the_orbitals_of_atoms[key1][key2]
                        name_orb_b = check_orbital_box[i].text()
                        max_orbital_share_b = max(marker_size_b.values())
                        max_orbital_share_b = max(max_orbital_share_b)

                    if b == 3:
                        marker_size_c = share_of_the_orbitals_of_atoms[key1][key2]
                        name_orb_c = check_orbital_box[i].text()
                        max_orbital_share_c = max(marker_size_c.values())
                        max_orbital_share_c = max(max_orbital_share_c)

            for (band, a_list), (band, b_list), (band, c_list) in zip(marker_size_a.items(), marker_size_b.items(), marker_size_c.items()):
                for a, b, c in zip(a_list, b_list, c_list):
                    color_tuple = (int(a / max_orbital_share_a * 255), int(b / max_orbital_share_b * 255), int(c / max_orbital_share_c * 255))
                    color_tuple = pc.label_rgb(color_tuple)
                    text = "Orbitals share:<br>" + name_orb_a + ": " + str(a) + ",<br>" + name_orb_b + ": " + str(b) + ",<br>" + name_orb_c + ": " + str(c)
                    AO_share[band].append(text)
                    new_colorscale[band]['Color scale'].append(color_tuple)

            energy_df['Colorscale'] = (pd.DataFrame(new_colorscale)).transpose()

            if self.dialog.energy_eV.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eV'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}', hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))
                fig.update_yaxes(title_text='E-Ef [eV]')

            elif self.dialog.fermi_no_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in Ry'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}', hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))

                fig.update_yaxes(title_text='E [Ry]')

            elif self.dialog.fermi_yes_button.isChecked():

                for band in range(0, len(energy_df.index)):
                    fig.add_trace(go.Scatter(x=k_path, y=energy_df['Energy in eRy - Fermi at 0'][band],
                                             text=k_vec['K-Vec'], mode='markers',
                                             marker=dict(color=energy_df['Colorscale'][band]),
                                             name=f'Band {band + 1}', hovertext=AO_share[f'Band {1 + band}'],
                                             hovertemplate="Energy: %{y:.4f} [eV] <br>k-vec%{text} <br>%{hovertext}"))

                fig.update_yaxes(title_text='E-Ef [Ry]')

            fig.update_layout(plot_bgcolor="white", hoverlabel=dict(bgcolor="ghostwhite"),
                              modebar_activecolor="DarksLateGray")

            fig.update_layout(
                updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                args=[{'mode': "markers"}],
                                label="markers",
                                method="restyle"
                            ),
                            dict(
                                args=[{'mode': "markers+lines", 'line.color': "black", 'line.width': "1.5"}],
                                label="markers+lines",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.08,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'plot_bgcolor': "white"}],
                                label="white",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "ivory"}],
                                label="ivory",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "whitesmoke"}],
                                label="whitesmoke",
                                method="relayout"
                            ),
                            dict(
                                args=[{'plot_bgcolor': "snow"}],
                                label="snow",
                                method="relayout"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.37,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=[{'marker.size': 6}],
                                label="6",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 4}],
                                label="4",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 5}],
                                label="5",
                                method="restyle"
                            ),
                            dict(
                                args=[{'marker.size': 7}],
                                label="7",
                                method="restyle"
                            ),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.64,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    ),
                    dict(
                        buttons=list([
                            dict(
                                args=["showlegend", True],
                                label="True",
                                method="restyle"
                            ),
                            dict(
                                args=["showlegend", False],
                                label="False",
                                method="restyle"
                            )
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.85,
                        xanchor="left",
                        y=1.12,
                        yanchor="top"
                    )
                ]

            )
            fig.update_layout(
                annotations=[
                    dict(text="Mode:", x=0.02, xref="paper", y=1.09, yref="paper",
                         align="left", showarrow=False),
                    dict(text="Background<br>color:", x=0.27, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Marker<br>size:", x=0.57, xref="paper", y=1.10,
                         yref="paper", showarrow=False),
                    dict(text="Show<br>legend:", x=0.8, xref="paper", y=1.10, yref="paper",
                         showarrow=False)
                ])

            fig.add_annotation(
                text=f'\U0001F534 - {name_orb_a}<br>\U0001F7E2 - {name_orb_b}<br>\U0001F535 - {name_orb_c}',
                align='left',
                showarrow=False,
                xref='paper',
                yref='paper',
                x=1,
                y=0,
                bordercolor='dimgrey',
                borderwidth=1,
                bgcolor="white"
            )

            fig.update_xaxes(title_text='k-vec', showticklabels=False, showgrid=False, mirror=True,
                             showline=True,
                             linecolor="DimGrey", range=[0, k_path[-1]])

            config = {
                'toImageButtonOptions': {
                    'filename': compound_name,
                    'height': 700,
                    'width': 900,
                    'scale': 3
                }
            }

            try:
                fig.update_yaxes(title_text='E-Ef [eV]', showgrid=False, mirror=True, showline=True,
                                 linecolor="DimGrey",
                                 ticks="outside", range=[min_range, max_range])
            except(UnboundLocalError):
                pass

            if self.dialog.energy_eV.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_yes_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=0, y1=0,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            elif self.dialog.fermi_no_button.isChecked():
                fig.add_shape(type='line', x0=0, x1=k_path[-1], y0=fermi_Energy, y1=fermi_Energy,
                              line=dict(color="rosybrown", dash="dash"), name="Fermi energy")

            fig.update_layout(
                font_family="Tahoma",
                font_color="dimgrey"
            )

            for i in range(0, len(legend_values)):
                fig.add_vline(x=legend_values[i], line_width=1, line_color="dimgrey",
                              annotation_text=high_symmetry_points[i],
                              annotation_position="bottom")

            try:
                if self.dialog.energy_eV.isChecked():
                    max_available_energy = max_energy_in_eV
                    min_available_energy = min_energy_in_eV
                elif self.dialog.fermi_no_button.isChecked():
                    max_available_energy = max_energy_in_Ry
                    min_available_energy = min_energy_in_Ry
                elif self.dialog.fermi_yes_button.isChecked():
                    max_available_energy = max_energy_in_Ry - fermi_Energy
                    min_available_energy = min_energy_in_Ry - fermi_Energy

                if max_range > max_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your max range is higher than max available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif min_range < min_available_energy:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Your min range is lower than min available energy.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
                elif max_range > min_range:
                    fig.show(config=config)
                else:
                    error_dialog = QMessageBox()
                    error_dialog.setWindowIcon(QtGui.QIcon('Images/N.png'))
                    error_dialog.setIcon(QMessageBox.Warning)
                    error_dialog.setWindowTitle("Error Message")
                    error_dialog.setText('Highest energy range is lower than lowest energy range.\n'
                                         'Please correct the input energy range.')
                    error_dialog.exec_()
            except(UnboundLocalError):
                pass

        #ZABEZPIECZAM BO CZASEM SIĘ USTAWIA CZTERY

        elif k == 4:
            for i, v in enumerate(check_orbital_box):
                check_orbital_box[i].setChecked(False)

def main():

    app = QApplication(sys.argv)
    window = FirstWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
