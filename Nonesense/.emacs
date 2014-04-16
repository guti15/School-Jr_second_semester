(add-to-list 'load-path "~/emacs-w3m")
(require 'w3m-load)
;;------------------------------------------------
;;      El -get Package code: 

(add-to-list 'load-path "~/.emacs.d/el-get/el-get")

(unless (require 'el-get nil 'noerror)
  (with-current-buffer
      (url-retrieve-synchronously
       "https://raw.github.com/dimitri/el-get/master/el-get-install.el")
    (goto-char (point-max))
    (eval-print-last-sexp)))

(add-to-list 'el-get-recipe-path "~/.emacs.d/el-get-user/recipes")
(el-get 'sync)

;;------------------------------------------------
;;-----Set ido mode-------------------------------
(require 'ido)
(ido-mode t)

;;----------------------------------------------
;; new code : 
(require 'powerline)
;;colors
(setq powerline-color1 "#222") ;; dark grey
(setq powerline-color2 "#444")
;; shape ....
(setq powerline-arrow-shape 'arrow) ;; mirrored arrows

;; ----------------------------  END Power line 

;;-----------------------------------------------
;;-----------------------------------------------
(package-initialize)
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector ["black" "#d55e00" "#009e73" "#f8ec59" "#0072b2" "#cc79a7" "#56b4e9" "white"])
 '(custom-enabled-themes nil)
 '(custom-safe-themes (quote ("72a303bf550bbf59310faad29e26a8c47b09e3215b0774fdd558f10be5e2f57a" default)))
 '(menu-bar-mode t)
 '(tool-bar-mode nil)
 '(global-linum-mode 1)
;;------------------------------------------------
;; -----This was meant for auto completion ---- 

;; (add-to-list 'load-path "/path/to/anything/")
;; (require 'anything)
;; (require 'anything-config) (require 'anything-ipython)
;; (when(require 'anything-show-completion nil t) 
;; (use-anything-show-completion 'anything-ipython-complete
;; 				'(length initial-pattern)))
;;-------------------------------------------------
(require 'package)
(add-to-list 'package-archives 
    '("marmalade" .
      "http://marmalade-repo.org/packages/"))
(package-initialize)

;; ------------------------------------------------

;; ------------------------------------------------
;; --------------   Power Line   ------------------

(require 'powerline)
;; colors...
(setq powerline-color1 "#222")      ;; dark grey; 
(setq powerline-color2 "#444")      ;; slightly lighter grey
;; shape...
(setq powerline-arrow-shape 'arrow14) ;; mirrored arrows, 
;; see below for the shape options

;; ------------------------------------------------


 '(custom-set-faces
 ;; custom-set-faces was added by Custom.                            
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.                            
 ;; If there is more than one, they won't work right.                   
 '(default ((t (:inherit nil :stipple nil :inverse-video nil :box nil :strike-through nil :overline nil :underline nil :slant normal :weight normal :height\
 1 :width normal :foundry "default" :family "default")))))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-archives (quote (("marmalade" . "http://marmalade-repo.org/packages/") ("gnu" . "http://elpa.gnu.org/packages/") ("marmalade" . "http://marmalade-repo.org/packages/")))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
