/**
 * Created by JasonG on 2/17/19.
 */

var base64Image

$("#image-selector").change(function(){
    var reader = new FileReader()

    reader.onload = function(e) {

        var dataURL = reader.result
        // Show image
        $("#selected-image").attr("src", dataURL)
        // Get base64Image data
        // Currently ONLY support .jpg file
        // For .png file, we just need
        // data:image/png;base64
        base64Image = dataURL.replace("data:image/jpeg;base64,", "")
        base64Image = base64Image.replace("data:image/jpg;base64,", "")
        base64Image = base64Image.replace("data:image/png;base64,", "")
        console.log(base64Image)
    }

    reader.readAsDataURL($("#image-selector")[0].files[0])
})

