;;; drupal-spell-autoloads.el --- automatically extracted autoloads
;;
;;; Code:


;;;### (autoloads (drupal-spell-enable) "drupal-spell" "drupal-spell.el"
;;;;;;  (21224 41306 0 0))
;;; Generated autoloads from drupal-spell.el

(autoload 'drupal-spell-enable "drupal-spell" "\
Enable Drupal dictionary as aspell extra dictionary in current buffer.

\(fn)" t nil)

(add-hook 'drupal-mode-hook 'drupal-spell-enable)

;;;***

;;;### (autoloads nil nil ("drupal-spell-pkg.el") (21224 41306 47671
;;;;;;  0))

;;;***

(provide 'drupal-spell-autoloads)
;; Local Variables:
;; version-control: never
;; no-byte-compile: t
;; no-update-autoloads: t
;; coding: utf-8
;; End:
;;; drupal-spell-autoloads.el ends here
