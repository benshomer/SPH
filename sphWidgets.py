#-*= coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango, Gdk, GdkPixbuf

targetInfoDialog = '''
<interface>
  <object class="GtkDialog" id="targetAnalysisDialog_%s">
    <property name="can_focus">False</property>
    <property name="type_hint">dialog</property>
    <child type="titlebar">
      <object class="GtkBox">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">Provide Target Information</property>
            <attributes>
              <attribute name="weight" value="bold"/>
            </attributes>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
    <child internal-child="vbox">
      <object class="GtkBox">
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox">
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <placeholder/>
            </child>
            <child>
              <object class="GtkButton" id="runTarget_%s">
                <property name="label" translatable="yes">ANALYSE</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="image">Apply</property>
                <property name="image_position">right</property>
                <signal name="clicked" handler="runTarget" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkGrid">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Name of Target</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkEntry" id="targetName">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">%s</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">0</property>
              </packing>
            </child>
           <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Color Scale Min Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="scmin">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">0.0000000</property>
                <property name="adjustment">scmin_adj</property>
                <property name="digits">7</property>
                <property name="numeric">True</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Color Scale Max Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="margin_left">3</property>
                <property name="margin_right">4</property>
                <property name="label" translatable="yes">Color Scale Tick Start At Zero?</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Plot X Scale Min Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">4</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Plot X Scale Max Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">5</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Plot Y Scale Min Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">6</property>
              </packing>
            </child>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Plot Y Scale Max Tick Value</property>
              </object>
              <packing>
                <property name="left_attach">0</property>
                <property name="top_attach">7</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="scmax">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">0.0000000</property>
                <property name="input_purpose">number</property>
                <property name="adjustment">scmax_adj</property>
                <property name="digits">7</property>
                <property name="numeric">True</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkCheckButton" id="stzero">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">False</property>
                <property name="margin_left">23</property>
                <property name="margin_top">7</property>
                <property name="margin_bottom">7</property>
                <property name="image_position">right</property>
                <property name="active">True</property>
                <property name="draw_indicator">True</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="plxmin">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">40</property>
                <property name="input_purpose">number</property>
                <property name="adjustment">plxmin_adj</property>
                <property name="numeric">True</property>
                <property name="value">40</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">4</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="plxmax">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">140</property>
                <property name="input_purpose">number</property>
                <property name="adjustment">plxmax_adj</property>
                <property name="numeric">True</property>
                <property name="value">140</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">5</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="plymin">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">40</property>
                <property name="input_purpose">number</property>
                <property name="adjustment">plymin_adj</property>
                <property name="numeric">True</property>
                <property name="value">40</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">6</property>
              </packing>
            </child>
            <child>
              <object class="GtkSpinButton" id="plymax">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="text" translatable="yes">180</property>
                <property name="input_purpose">number</property>
                <property name="adjustment">plymax_adj</property>
                <property name="numeric">True</property>
                <property name="value">180</property>
              </object>
              <packing>
                <property name="left_attach">1</property>
                <property name="top_attach">7</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
'''

def empty():
    pass

SPHdialog_template = '''
<interface>
  <object class="GtkDialog" id="SPHdialog_%s">
    <property name="can_focus">False</property>
    <property name="modal">True</property>
    <property name="window_position">center</property>
    <property name="type_hint">dialog</property>
    <property name="gravity">center</property>
    <child>
      <placeholder/>
    </child>
    <child internal-child="vbox">
      <object class="GtkBox">
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child internal-child="action_area">
          <object class="GtkButtonBox">
            <property name="can_focus">False</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="cancelSH_%s">
                <property name="label">gtk-cancel</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
                <signal name="activate" handler="cancelSH_params" swapped="no"/>
                <signal name="clicked" handler="cancelSH_params" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="runSPH_%s">
                <property name="label" translatable="yes">&lt;&lt;RUN&gt;&gt;</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <signal name="activate" handler="runSPH" swapped="no"/>
                <signal name="clicked" handler="runSPH" swapped="no"/>
              </object>
              <packing>
                <property name="expand">True</property>
                <property name="fill">True</property>
                <property name="position">1</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">False</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="orientation">vertical</property>
            <child>
              <object class="GtkLabel">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Real Wigner Rotation Matrix Elements, D&lt;sub&gt;L,K&lt;/sub&gt;</property>
                <property name="use_markup">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <object class="GtkBox">
                <property name="name">RankBox_%s</property>
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <child>
                  <object class="GtkLabel">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label" translatable="yes">Rank  </property>
                    <style>
                      <class name="rankLabel"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="rankSelect_%s">
                    <property name="label" translatable="yes">1</property>
                    <property name="name">1</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">False</property>
                    <signal name="toggled" handler="changeRankSelect" swapped="no"/>
                    <style>
                      <class name="rankValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton">
                    <property name="label" translatable="yes">2</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">False</property>
                    <property name="group">rankSelect_%s</property>
                    <signal name="toggled" handler="changeRankSelect" swapped="no"/>
                    <style>
                      <class name="rankValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton">
                    <property name="label" translatable="yes">3</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">False</property>
                    <property name="group">rankSelect_%s</property>
                    <signal name="toggled" handler="changeRankSelect" swapped="no"/>
                    <style>
                      <class name="rankValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton">
                    <property name="label" translatable="yes">4</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">False</property>
                    <property name="group">rankSelect_%s</property>
                    <signal name="toggled" handler="changeRankSelect" swapped="no"/>
                    <style>
                      <class name="rankValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">True</property>
                    <property name="fill">True</property>
                    <property name="position">4</property>
                  </packing>
                </child>
                <child>
                  <placeholder/>
                </child>
                <style>
                  <class name="rankBox_cs"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkBox">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="homogeneous">True</property>
                <child>
                  <object class="GtkLabel">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="label" translatable="yes">Order Select:  </property>
                    <style>
                      <class name="orderLabel"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="noneOrder">
                    <property name="label" translatable="yes">Clear</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="active">True</property>
                    <property name="draw_indicator">True</property>
                    <signal name="clicked" handler="changeOrderSelect" swapped="no"/>
                    <style>
                      <class name="orderValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="oddOrder">
                    <property name="label" translatable="yes">Odd</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">noneOrder</property>
                    <signal name="clicked" handler="changeOrderSelect" swapped="no"/>
                    <style>
                      <class name="orderValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">2</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="evenOrder">
                    <property name="label" translatable="yes">Even</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">noneOrder</property>
                    <signal name="clicked" handler="changeOrderSelect" swapped="no"/>
                    <style>
                      <class name="orderValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">3</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkRadioButton" id="contOrder">
                    <property name="label" translatable="yes">Select All</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="receives_default">False</property>
                    <property name="draw_indicator">True</property>
                    <property name="group">noneOrder</property>
                    <signal name="clicked" handler="changeOrderSelect" swapped="no"/>
                    <style>
                      <class name="orderValue"/>
                    </style>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">True</property>
                    <property name="position">4</property>
                  </packing>
                </child>
                <style>
                  <class name="orderBox_cs"/>
                </style>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">3</property>
              </packing>
            </child>
            <child>
              <object class="GtkScrolledWindow">
                <property name="width_request">550</property>
                <property name="height_request">540</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="shadow_type">in</property>
                <child>
                  <object class="GtkViewport">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkBox" id="Ylunchbox_%s">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="orientation">vertical</property>
                        <child>
                          <object class="GtkBox">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="orientation">vertical</property>
                            <child>
                              <object class="GtkBox" id="Y00box">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <child>
                                  <object class="GtkCheckButton" id="Y00chk">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <property name="receives_default">False</property>
                                    <property name="draw_indicator">True</property>
                                  </object>
                                  <packing>
                                    <property name="expand">False</property>
                                    <property name="fill">True</property>
                                    <property name="position">0</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkImage" id="Y00img">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="pixbuf">images/Y10.png</property>
                                  </object>
                                  <packing>
                                    <property name="expand">False</property>
                                    <property name="fill">True</property>
                                    <property name="position">1</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="Y00sym">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Ag</property>
                                    <property name="justify">center</property>
                                    <attributes>
                                      <attribute name="font-desc" value="Times New Roman, Bold 14"/>
                                      <attribute name="weight" value="bold"/>
                                    </attributes>
                                  </object>
                                  <packing>
                                    <property name="expand">True</property>
                                    <property name="fill">True</property>
                                    <property name="pack_type">end</property>
                                    <property name="position">2</property>
                                  </packing>
                                </child>
                              </object>
                              <packing>
                                <property name="expand">False</property>
                                <property name="fill">True</property>
                                <property name="position">0</property>
                              </packing>
                            </child>
                            <child>
                              <object class="GtkBox">
                                <property name="visible">True</property>
                                <property name="can_focus">False</property>
                                <child>
                                  <object class="GtkLabel">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">Coefficient</property>
                                  </object>
                                  <packing>
                                    <property name="expand">False</property>
                                    <property name="fill">True</property>
                                    <property name="position">0</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkLabel" id="Y00_Clbl">
                                    <property name="visible">True</property>
                                    <property name="can_focus">False</property>
                                    <property name="label" translatable="yes">&lt;i&gt;&lt;b&gt;C&lt;sub&gt;0,0&lt;/sub&gt;&lt;/b&gt;&lt;/i&gt;</property>
                                    <property name="use_markup">True</property>
                                  </object>
                                  <packing>
                                    <property name="expand">False</property>
                                    <property name="fill">True</property>
                                    <property name="position">1</property>
                                  </packing>
                                </child>
                                <child>
                                  <object class="GtkScale" id="Y00_coef">
                                    <property name="visible">True</property>
                                    <property name="can_focus">True</property>
                                    <property name="adjustment">coefficientAdj</property>
                                    <property name="round_digits">0</property>
                                    <property name="digits">0</property>
                                    <property name="value_pos">left</property>
                                  </object>
                                  <packing>
                                    <property name="expand">True</property>
                                    <property name="fill">True</property>
                                    <property name="padding">6</property>
                                    <property name="position">2</property>
                                  </packing>
                                </child>
                              </object>
                              <packing>
                                <property name="expand">False</property>
                                <property name="fill">True</property>
                                <property name="position">1</property>
                              </packing>
                            </child>
                            <style>
                              <class name="orderBox"/>
                            </style>
                          </object>
                          <packing>
                            <property name="expand">False</property>
                            <property name="fill">True</property>
                            <property name="position">0</property>
                          </packing>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                        <child>
                          <placeholder/>
                        </child>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">True</property>
                <property name="position">4</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>

  <object class="GtkAccelGroup" id="accelgroup1"/>
  <object class="GtkAction" id="action1"/>
  <object class="GtkAdjustment" id="coefficientAdj">
    <property name="lower">-30</property>
    <property name="upper">30</property>
    <property name="step_increment">1</property>
    <property name="page_increment">10</property>
  </object>

</interface>
'''

def empty1():
    pass


sphExpPopup_template = '''
<interface>
 <object class="GtkImage" id="reRun">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-refresh</property>
  </object>
  <object class="GtkImage" id="clone">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-copy</property>
  </object>
  <object class="GtkImage" id="export">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="stock">gtk-floppy</property>
  </object>
  <object class="GtkImage" id="trash">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="icon_name">user-trash</property>
    <property name="use_fallback">True</property>
  </object>
  <object class="GtkMenuBar" id="expResultMenu">
    <property name="width_request">24</property>
    <property name="height_request">24</property>
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="valign">start</property>
    <property name="margin_top">12</property>
    <child>
      <object class="GtkMenuItem">
      <property name="width_request">24</property>
      <property name="height_request">24</property>
      <property name="visible">True</property>
      <property name="can_focus">False</property>
      <property name="valign">start</property>
      <property name="margin_top">12</property>
      <property name="label" translatable="yes">☰</property>
      <property name="use_underline">True</property>
      <child type="submenu">
        <object class="GtkMenu">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <child>
          <object class="GtkImageMenuItem" id="rerunExpResult">
          <property name="label" translatable="yes">reRun</property>
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          <property name="image">reRun</property>
          <property name="use_stock">False</property>
          <signal name="activate" handler="exp_rerun" swapped="no"/>
          </object>
        </child>
        <child>
          <object class="GtkImageMenuItem" id="cloneExpResult">
          <property name="label" translatable="yes">Clone</property>
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          <property name="image">clone</property>
          <property name="use_stock">False</property>
          <signal name="activate" handler="exp_clone" swapped="no"/>
          </object>
        </child>
        <child>
          <object class="GtkSeparatorMenuItem">
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          </object>
         </child>
         <child>
          <object class="GtkImageMenuItem" id="exportExpResult">
          <property name="label" translatable="yes">Export</property>
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          <property name="image">export</property>
          <property name="use_stock">False</property>
          <signal name="activate" handler="exp_export" swapped="no"/>
          </object>
        </child>
        <child>
          <object class="GtkSeparatorMenuItem">
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          </object>
        </child>
        <child>
          <object class="GtkImageMenuItem" id="deleteExpResult">
          <property name="label" translatable="yes">Delete</property>
          <property name="visible">True</property>
          <property name="can_focus">False</property>
          <property name="image">trash</property>
          <property name="use_stock">False</property>
          <signal name="activate" handler="exp_delete" swapped="no"/>
          </object>
        </child>
      </object>
    </child>
    </object>
   </child>
  </object>

</interface>
'''
