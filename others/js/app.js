// // Import vendor jQuery plugin example
// import '~/app/libs/mmenu/dist/mmenu.js'

document.addEventListener('DOMContentLoaded', () => {


	// навешивает span на буквы О в лого
	$('.logo-litera').each(function() {
		// берём в ths чтобы было удобнее работать
		var ths = $(this);
		// jQuery метод .html() задает содержимое выбранных элементов, или возвращает значение первого элемента в наборе.
		// внутри метода .html() берём всё содержимое элемента, и методом .replace() замещаем О на О в теге спан
		ths.html(ths.html().replace('O', '<span>O</span>'))
	});


	// открывает-скрывает поле ввода по клику на иконку поиска
	$('.search').on('click', function() {
		// функция stop() останавливает действие при отводе курсора (чтоб долго не спамилось)
		$('.search-field').stop().slideToggle();
		// устанавливает фокус в поле ввода после открытия
		$('.search-field input[type=text]').focus();
	});


	// скрывает окно поиска по нажатию клавиши Escape
	// keyup перехватывает события нажатия кнопки и передаёт их в анонимную функцию
	$(document).keyup(function(e) {
		// если код события равен коду клавиши Escape - 27
		if (e.keyCode == 27) {
			$('.search-field').slideUp(); // скрываем окно поиска
		}
		// к этому же селектору (всему окну), привязываем событие .click()
	}).click(function() {
		$('.search-field').slideUp(); // скрываем окно поиска
	});


	// перехватываем и отменяем событие если клик происходит по враперу окна поиска
	$('.search-wrap').click(function(e) {
		// Propagation — это распространение событий. Метод stopPropagation используется для
		// предотвращения распространения (всплытия) событий, когда событие запускается на отдельном элементе.
		// В JavaScript, когда событие запускается на одном элементе, оно всплывает вверх по дереву родительских
		// элементов. Если элемент с событием находится внутри родительского контейнера, родитель тоже получает
		// это событие.
		e.stopPropagation();
	});


	// after(content) — вставляет контент после каждого элемента из выборки
	$('.top-line').after('<div class="mobile-menu d-lg-none">');
	// клонируем меню и добавляем в див .mobile-menu
	$('.top-menu').clone().appendTo('.mobile-menu')
	$('.mobile-menu-button').click(function() {
		$('.mobile-menu').stop().slideToggle()
	})

	// добавление .hover к заголовку айтема при :hover на изображение(index reviews)
	$('.col-item').on('mouseenter', function() {
		var ths = $(this)
		var lnk = ths.closest('.col-item').find('h4 a')
		lnk.addClass('hover')
		console.log('true')
	}).on('mouseleave', function() {
		var ths = $(this)
		var lnk = ths.closest('.col-item').find('h4 a')
		lnk.removeClass('hover')
		})

	// $('.mobile-menu-button').click(function() {
	// 	$('.mobile-menu .top-menu').toggleClass('visually-hidden').stop().slideToggle();
	// })
	$("body").prognroll({
		height: 3,
		color: "#ec1c1c",
		custom: false
	});

});
