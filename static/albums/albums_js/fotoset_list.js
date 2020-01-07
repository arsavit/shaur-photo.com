$(document).ready(function () {

    $('.ars-panel-heading').click(function () {
        $(this).toggleClass('in').next().slideToggle();
        $('.ars-panel-heading').not(this).removeClass('in').next().slideUp();
        return false;
    });
    'use strict';

    function _classCallCheck(instance, Constructor) {
        if (!(instance instanceof Constructor)) {
            throw new TypeError("Cannot call a class as a function");
        }
    }

// ——————————————————————————————————————————————————
// TextScramble
// ——————————————————————————————————————————————————

    var TextScramble = function () {
        function TextScramble(el) {
            _classCallCheck(this, TextScramble);

            this.el = el;
            this.chars = '!<>-_\\/[]{}—=+*^?#________';
            this.update = this.update.bind(this);
        }

        TextScramble.prototype.setText = function setText(newText) {
            var _this = this;

            var oldText = this.el.innerText;
            var length = Math.max(oldText.length, newText.length);
            var promise = new Promise(function (resolve) {
                return _this.resolve = resolve;
            });
            this.queue = [];
            for (var i = 0; i < length; i++) {
                var from = oldText[i] || '';
                var to = newText[i] || '';
                var start = Math.floor(Math.random() * 40);
                var end = start + Math.floor(Math.random() * 40);
                this.queue.push({from: from, to: to, start: start, end: end});
            }
            cancelAnimationFrame(this.frameRequest);
            this.frame = 0;
            this.update();
            return promise;
        };

        TextScramble.prototype.update = function update() {
            var output = '';
            var complete = 0;
            for (var i = 0, n = this.queue.length; i < n; i++) {
                var _queue$i = this.queue[i];
                var from = _queue$i.from;
                var to = _queue$i.to;
                var start = _queue$i.start;
                var end = _queue$i.end;
                var char = _queue$i.char;

                if (this.frame >= end) {
                    complete++;
                    output += to;
                } else if (this.frame >= start) {
                    if (!char || Math.random() < 0.28) {
                        char = this.randomChar();
                        this.queue[i].char = char;
                    }
                    output += '<span class="dud">' + char + '</span>';
                } else {
                    output += from;
                }
            }
            this.el.innerHTML = output;
            if (complete === this.queue.length) {
                this.resolve();
            } else {
                this.frameRequest = requestAnimationFrame(this.update);
                this.frame++;
            }
        };

        TextScramble.prototype.randomChar = function randomChar() {
            return this.chars[Math.floor(Math.random() * this.chars.length)];
        };

        return TextScramble;
    }();

// ——————————————————————————————————————————————————
// Example
// ——————————————————————————————————————————————————

    var phrases = ['<div class="social-script"><a target="_blank" class="text-vk" href="https://vk.com/club134565385"><i class="fab fa-vk"></i> Вконтакте </a> <a target="_blank" class="text-inst" href="https://www.instagram.com/sviatlana_haurylavets/"><i class="fab fa-instagram"></i> Инстаграм</a> <a class="text-tel" href="tel:+375291234567"><i class="fas fa-phone-alt"></i>Телефон</a></div>', '<a target="_blank" class="text-vk" href="https://vk.com/club134565385"><i class="fab fa-vk"></i> Вконтакте </a>', '<p class="text-p-inst"><a target="_blank" class="text-inst" href="https://www.instagram.com/sviatlana_haurylavets/"><i class="fab fa-instagram"></i> Инстаграм</a></p>', '<a class="text-tel" href="tel:+375291234567"><i class="fas fa-phone-alt"></i>Телефон</a></div>', '<p class="text-p-inst"><a target="_blank" class="text-inst" href="https://www.instagram.com/sviatlana_haurylavets/"><i class="fab fa-instagram"></i> Посмотреть</a></p>', '<a target="_blank" class="text-vk" href="https://vk.com/club134565385"><i class="fab fa-vk"></i> Написать </a>', '<a class="text-tel" href="tel:+375291234567"><i class="fas fa-phone-alt"></i>Позвонить</a></div>', '<div class="social-script"><a target="_blank" class="text-vk" href="https://vk.com/club134565385"><i class="fab fa-vk"></i> Vkontakte </a> <a target="_blank" class="text-inst" href="https://www.instagram.com/sviatlana_haurylavets/"><i class="fab fa-instagram"></i>Instagram</a> <a class="text-tel" href="tel:+375291234567"><i class="fas fa-phone-alt"></i>Phone</a></div>', '<a target="_blank" class="text-vk" href="https://vk.com/club134565385"><i class="fab fa-vk"></i> Vkontakte </a>', '<a class="text-tel" href="tel:+375291234567"><i class="fas fa-phone-alt"></i>Phone</a></div>', '<p class="text-p-inst"><a target="_blank" class="text-inst" href="https://www.instagram.com/sviatlana_haurylavets/"><i class="fab fa-instagram"></i>Instagram</a></p>', ''];

    var el = document.querySelector('.text');
    var fx = new TextScramble(el);

    var counter = 0;
    var next = function next() {
        fx.setText(phrases[counter]).then(function () {
            setTimeout(next, 2500);
        });
        counter = (counter + 1) % phrases.length;
    };

    next();
});