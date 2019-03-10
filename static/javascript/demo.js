/**
 * Created by JasonG on 2/26/19.
 */

console.log('demo page JS loaded...')

var id = 0;
sample_photo_img_url_list = [
    "https://i.ibb.co/30zgK2H/1-beach-miami-south-beach.jpg",
    "https://i.ibb.co/47hbcJb/2-rose-garden.jpg",
    "https://i.ibb.co/C1LsDG7/3-green-park.jpg",
    "https://i.ibb.co/9sL96dj/4-city-street.jpg",
    "https://i.ibb.co/HCqd9FB/5-indoor-coffee-shop.jpg",
    "https://i.ibb.co/yyWPd3m/6-Ins-wall.jpg"
]

$('.demo-photo').click(function() {
    console.log('photo clicked...')
    $('.demo-photo').removeClass('photo-selected')
    $(this).addClass('photo-selected')
    // console.log(this.id)
    id = this.id.split("_")[1]
});

$('#Sample_Predict').click(function(e) {
    // if(id == - 1) id = 0;
    sample_photo_img_url = sample_photo_img_url_list[id]
    e.preventDefault();

    var imageURL = {
        image_url: sample_photo_img_url
    }
    $.post("http://127.0.0.1:5000/predict", JSON.stringify(imageURL), function(response){
        // console.log(response)
        $('.demo-section3-wrapper').empty()
        $('.demo-section3-wrapper').append('<h1> Our Recommendations  </h1>')

        response.prediction.forEach(function(element) {
            // console.log(element)
            $('.demo-section3-wrapper').append('<div> <img src="/static/images/two_hundred/' + element + '.jpg"/></div>')
        })
    })

    $("html, body").animate({ scrollTop: $('#Demo_Section3').offset().top }, 2000, 'linear');
})

var input_url = ''

$('.photo-form-button').click(function() {
    // console.log('Use this photo clicked...')
    input_url = $('#input_url').val();
    // console.log(input_url)
    $(".input-image-wrapper img").attr("src", input_url)
});

$('#Photo_Predict').click(function(e) {
    // if(id == - 1) id = 0;
    // sample_photo_img_url = sample_photo_img_url_list[id]
    // user_photo_img_url = "https://i.ibb.co/30zgK2H/1-beach-miami-south-beach.jpg"
    e.preventDefault();
    if(input_url.length == 0) {
        // alert("Please try a valid image url")
        alert("Image url is empty.")
    } else {
        input_split = input_url.split(".")
        file_type = input_split[input_split.length - 1]
        if(file_type != "png" && file_type != "jpg" && file_type != "jpeg") {
            alert("Please try a valid image file .png .jpg .jpeg")
        } else {
            var imageURL = {
                image_url: input_url
            }
            $.post("http://127.0.0.1:5000/predict", JSON.stringify(imageURL), function(response){
                // console.log(response)
                $('.demo-section3-wrapper').empty()
                $('.demo-section3-wrapper').append('<h1> Our Recommendations  </h1>')

                response.prediction.forEach(function(element) {
                    // console.log(element)
                    $('.demo-section3-wrapper').append('<div> <img src="/static/images/two_hundred/' + element + '.jpg"/></div>')
                })
            })

            $("html, body").animate({ scrollTop: $('#Demo_Section3').offset().top }, 2000, 'linear');
        }
    }
})
