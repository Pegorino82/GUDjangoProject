window.onload = function () {
    $('.product-line').on('click', 'a', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/basket/",

            success: function (data) {
                $('.product-line').html(data.result);
            },
        });

        event.preventDefault();
    });
}

const Basket = ({quantity}) => (
    `
    ${ quantity }
    `
);

const renderData = res => {
    console.log(res.data.results);
    itm = res.data.results.map(Basket);
    basket_js = document.getElementById('basket_js');
    basket_js.innerHTML = itm;
}
