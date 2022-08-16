#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: cross-correlation
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import osmosdr
import time



from gnuradio import qtgui

class default(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "cross-correlation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("cross-correlation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "default")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 40000000
        self.fft_size = fft_size = 524288
        self.center_freq = center_freq = 937600000
        self.bandwidth = bandwidth = 50000

        ##################################################
        # Blocks
        ##################################################
        self._fft_size_tool_bar = Qt.QToolBar(self)

        if None:
            self._fft_size_formatter = None
        else:
            self._fft_size_formatter = lambda x: str(x)

        self._fft_size_tool_bar.addWidget(Qt.QLabel("'fft_size'"))
        self._fft_size_label = Qt.QLabel(str(self._fft_size_formatter(self.fft_size)))
        self._fft_size_tool_bar.addWidget(self._fft_size_label)
        self.top_layout.addWidget(self._fft_size_tool_bar)
        self._center_freq_tool_bar = Qt.QToolBar(self)

        if None:
            self._center_freq_formatter = None
        else:
            self._center_freq_formatter = lambda x: str(x)

        self._center_freq_tool_bar.addWidget(Qt.QLabel("'center_freq'"))
        self._center_freq_label = Qt.QLabel(str(self._center_freq_formatter(self.center_freq)))
        self._center_freq_tool_bar.addWidget(self._center_freq_label)
        self.top_layout.addWidget(self._center_freq_tool_bar)
        self._bandwidth_tool_bar = Qt.QToolBar(self)

        if None:
            self._bandwidth_formatter = None
        else:
            self._bandwidth_formatter = lambda x: str(x)

        self._bandwidth_tool_bar.addWidget(Qt.QLabel("'bandwidth'"))
        self._bandwidth_label = Qt.QLabel(str(self._bandwidth_formatter(self.bandwidth)))
        self._bandwidth_tool_bar.addWidget(self._bandwidth_label)
        self.top_layout.addWidget(self._bandwidth_tool_bar)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            32768, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            32000, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.05)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-200, 200)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(2) + " " + "bladerf=0,nchan=2"
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(bandwidth, 0)
        self.osmosdr_source_0.set_center_freq(100e6, 1)
        self.osmosdr_source_0.set_freq_corr(0, 1)
        self.osmosdr_source_0.set_dc_offset_mode(0, 1)
        self.osmosdr_source_0.set_iq_balance_mode(0, 1)
        self.osmosdr_source_0.set_gain_mode(False, 1)
        self.osmosdr_source_0.set_gain(10, 1)
        self.osmosdr_source_0.set_if_gain(20, 1)
        self.osmosdr_source_0.set_bb_gain(20, 1)
        self.osmosdr_source_0.set_antenna('', 1)
        self.osmosdr_source_0.set_bandwidth(0, 1)
        self.fft_vxx_1 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), True, 2)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), True, 2)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(fft_size)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.osmosdr_source_0, 1), (self.blocks_stream_to_vector_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "default")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        Qt.QMetaObject.invokeMethod(self._fft_size_label, "setText", Qt.Q_ARG("QString", str(self._fft_size_formatter(self.fft_size))))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        Qt.QMetaObject.invokeMethod(self._center_freq_label, "setText", Qt.Q_ARG("QString", str(self._center_freq_formatter(self.center_freq))))
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        Qt.QMetaObject.invokeMethod(self._bandwidth_label, "setText", Qt.Q_ARG("QString", str(self._bandwidth_formatter(self.bandwidth))))
        self.osmosdr_source_0.set_bandwidth(self.bandwidth, 0)




def main(top_block_cls=default, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
