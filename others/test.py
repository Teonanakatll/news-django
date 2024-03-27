def post_search(request):
    form = SearchForm()
    query = None
    count = None
    posts = []
    search_list = None
    title = 'Страница поиска.'
    first_cat, second_cat = get_random_category()

    # print(f"поисковый запрос {request.GET}")
    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            # количество постов на странице поиска
            first_page_num = 10
            query = form.cleaned_data['query']
            query = f'"{query}"'
            title = f'результаты поиска по запросу - {query}.'
            posts_all = Post.objects.search(query).filter(draft=False).select_related('category')
            count = posts_all.count()
            posts = posts_all[:first_page_num]



            #если количество результатов поиска больше количества постов установленных нами для
            #отображения на странице поиска +1, передаём оставшийся список на вьюху search_list для
            #отрисовки на шаблоне all-posts.html для корректной пагинации
            if len(posts_all) > first_page_num + 1:
                search_list = posts_all[10:]
                # список id всех статей по результатам поиска
                search_list = [n.id for n in search_list]

                # добавляем в конец списка поисковый запрос для отрисовки на вьюхе search_list
                print(search_list)
                search_list.append(query)

                # преобразование списка id в одну строку
                search_list = ' '.join(str(x) for x in search_list)

                # создаём список из строки и преобразуем в int
                # lst = search_list.split()
                # for i in range(len(lst)):
                #     if i > len(lst) - 1:
                #         lst[i] = int(lst[i])
                # вырезаем из списка поисковый запрос для отрисовке в title
                # string = lst.pop()

                # если количество результатов поиска больше количества постов установленных нами для
                # отображения на странице поиска +1, передаём оставшийся список на вьюху search_list для
                # отрисовки на шаблоне all-posts.html для корректной пагинации
                # if len(posts_all) > first_page_num + 1:
                #     search_list = posts_all[first_page_num:]
                #     # список id всех статей по результатам поиска
                #     search_list = [n.id.split('.')[2] for n in search_list]
                #     # print(f'search_list{search_list}')
                #     # добавляем в конец списка поисковый запрос для отрисовки на вьюхе search_list
                #     search_list.append(query)
                #     # преобразование списка id в одну строку
                #     search_list = ' '.join(str(x) for x in search_list)

    data = {
        'form': form,
        'title': title,
        'query': query,
        'count': count,
        'first_page_num': first_page_num,
        'search_list': search_list,
        'first_cat': first_cat,
        'second_cat': second_cat,
        'posts': posts
    }

    return render(request, 'news_app/search.html', context=data)