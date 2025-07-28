(function($) {
    $(document).ready(function() {
        const typeField = $('#id_type');
        const categoryField = $('#id_category');
        const subcategoryField = $('#id_subcategory');

        const allCategoryOptions = categoryField.find('option').clone();
        const allSubcategoryOptions = subcategoryField.find('option').clone();

        typeField.change(function() {
            const selectedTypeId = $(this).val();
            categoryField.empty();

            allCategoryOptions.each(function() {
                const option = $(this);
                const typeId = option.data('type-id');

                if (!typeId || typeId == selectedTypeId) {
                    categoryField.append(option.clone());
                }
            });

            categoryField.trigger('change'); // обновить подкатегории
        });

        categoryField.change(function() {
            const selectedCategoryId = $(this).val();
            subcategoryField.empty();

            allSubcategoryOptions.each(function() {
                const option = $(this);
                const categoryId = option.data('category-id');

                if (!categoryId || categoryId == selectedCategoryId) {
                    subcategoryField.append(option.clone());
                }
            });
        });
    });
})(django.jQuery);
