// window.onload = function () {
//     $('.product-line').on('click', 'a', function () {
//         var t_href = event.target;
//         console.log(t_href.href);
//
//         $('')
//
//         $.ajax({
//             url: "basket/edit" + t_href.href,
//             success: function (data) {
//                 $('.product-line').html(data.result);
//             },
//         });
//
//         event.preventDefault();
//     });
// }


//Foo = window.onload = function ({quantity, product_id}) {
//    $('.product-line').on('click', 'a', function () {
//        var t_href = event.target;
//        console.log(quantity, product_id);
//
//        $.ajax({
//            url: "edit/" + product_id + "/" + quantity + "/",
//            success: function (data) {
//                $('.product-line').html(data.result);
//            },
//        });
//
//        event.preventDefault();
//    });
//}
//
const Basket = ({quantity}) => (
    `
    ${ quantity }
    `
);

const renderData = res => {
    console.log(res.data.results);
//    res.data.results.map(Foo);
    itm = res.data.results.map(Basket).join(' / ');
    basket_js = document.getElementById('basket_js');
    basket_js.innerHTML = itm;
}

