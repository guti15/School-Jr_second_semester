;;; latex-preview-pane-autoloads.el --- automatically extracted autoloads
;;
;;; Code:


;;;### (autoloads (latex-preview-pane-mode latex-preview-pane-update-p
;;;;;;  latex-preview-pane-update latex-preview-update init-latex-preview-pane)
;;;;;;  "latex-preview-pane" "latex-preview-pane.el" (21245 18730
;;;;;;  0 0))
;;; Generated autoloads from latex-preview-pane.el

(add-hook 'latex-mode-hook (lambda nil (latex-preview-pane-mode t)))

(autoload 'init-latex-preview-pane "latex-preview-pane" "\


\(fn)" nil nil)

(if (eq window-system 'w32) (progn (setq view-buffer-command "start")))

(if (eq system-type 'darwin) (progn (setq view-buffer-command "open")))

(if (eq system-type 'gnu/linux) (progn (setq view-buffer-command "xdg-open")))

(if (eq system-type 'gnu/kfreebsd) (progn (setq view-buffer-command "xdg-open")))

(autoload 'latex-preview-update "latex-preview-pane" "\


\(fn)" t nil)

(autoload 'latex-preview-pane-update "latex-preview-pane" "\


\(fn)" t nil)

(autoload 'latex-preview-pane-update-p "latex-preview-pane" "\


\(fn)" nil nil)

(autoload 'latex-preview-pane-mode "latex-preview-pane" "\
Toggle Latex Preview Pane Mode.
     Interactively with no argument, this command toggles the mode.
     A positive prefix argument enables the mode, any other prefix
     argument disables it.  From Lisp, argument omitted or nil enables
     the mode, `toggle' toggles the state.
     
     When Latex Preview Pane mode is enabled, saving a latex file will cause 
     a PDF preview pane of your document to appear.

\(fn &optional ARG)" t nil)

;;;***

;;;### (autoloads nil nil ("latex-preview-pane-pkg.el") (21245 18730
;;;;;;  612944 0))

;;;***

(provide 'latex-preview-pane-autoloads)
;; Local Variables:
;; version-control: never
;; no-byte-compile: t
;; no-update-autoloads: t
;; coding: utf-8
;; End:
;;; latex-preview-pane-autoloads.el ends here
