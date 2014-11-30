(TeX-add-style-hook
 "Astro518TermPaper"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("aastex" "preprint" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "aastex"
    "aastex12"
    "graphicx")
   (LaTeX-add-labels
    "fig:optics"
    "tab:irac-sen"
    "fig:irac-lc"
    "fig:iraf-lc2")))

