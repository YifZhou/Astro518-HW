(TeX-add-style-hook
 "Astro518TermPaper"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("aastex" "preprint" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "aastex"
    "aastex12"
    "graphicx"
    "natbib")
   (LaTeX-add-labels
    "fig:optics"
    "sec:performance"
    "tab:irac-sen"
    "fig:nircam-sen"
    "fig:irac-lc"
    "fig:iraf-lc2"
    "fig:spec")
   (LaTeX-add-bibliographies
    "ref.bib")))

