(function($) {
    $(document).ready(function() {
        const categoryField = $('#id_category');
        const subcategoryField = $('#id_subcategory');

        const allOptions = subcategoryField.find('option').clone();

        categoryField.change(function() {
            const selectedCategoryId = $(this).val();
            subcategoryField.empty();

            allOptions.each(function() {
                const option = $(this);
                const categoryId = option.data('category-id');

                if (!categoryId || categoryId == selectedCategoryId) {
                    subcategoryField.append(option.clone());
                }
            });
        });
    });
})(django.jQuery);
