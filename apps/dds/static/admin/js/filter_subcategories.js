document.addEventListener('DOMContentLoaded', function() {
    const $ = django.jQuery || window.jQuery;
    if (!$) return;

    const typeField = $('#id_type');
    const categoryField = $('#id_category');
    const subcategoryField = $('#id_subcategory');

    // Кэшируем все опции
    const allCategoryOptions = categoryField.find('option').clone();
    const allSubcategoryOptions = subcategoryField.find('option').clone();

    // Валидация
    $('form').on('submit', function(e) {
        if (!typeField.val()) {
            alert('Выберите тип операции!');
            e.preventDefault();
            return;
        }
        if (!categoryField.val()) {
            alert('Выберите категорию!');
            e.preventDefault();
            return;
        }
    });

    // Фильтрация категорий по типу
    typeField.on('change', function() {
        const typeId = $(this).val();
        categoryField.empty();

        allCategoryOptions.each(function() {
            const option = $(this);
            const optionTypeId = option.data('type-id');

            if (!optionTypeId || optionTypeId == typeId) {
                categoryField.append(option.clone());
            }
        });

        categoryField.trigger('change');
    });

    // Фильтрация подкатегорий по категории
    categoryField.on('change', function() {
        const categoryId = $(this).val();
        subcategoryField.empty();

        allSubcategoryOptions.each(function() {
            const option = $(this);
            const optionCategoryId = option.data('category-id');

            if (!optionCategoryId || optionCategoryId == categoryId) {
                subcategoryField.append(option.clone());
            }
        });
    });

    // Инициализация при загрузке
    typeField.trigger('change');
});
