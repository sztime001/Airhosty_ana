# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:46:37 2018

@author: Sofei
"""

    function initNavigation() {
        $("#prev_mc_interval").off('click').on('click', e => {
            e.preventDefault();
            renderInterval(-NAVIGATION_INTERVAL * RENDER_INTERVAL);
        });

        $("#next_mc_interval").off('click').on('click', e => {
            e.preventDefault();
            renderInterval(NAVIGATION_INTERVAL * RENDER_INTERVAL);
        });
    }
