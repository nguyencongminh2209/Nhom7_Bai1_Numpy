function searchTour() {
    var selectedCity = document.getElementById("citySelect").value;
    var numberOfPeople = document.getElementById("numberOfPeople").value;
    var departureDate = document.getElementById("departureDate").value;
    var returnDate = document.getElementById("returnDate").value;
    var cityInfoDiv = document.getElementById("cityInfo");

    // Xóa thông tin hiện tại
    cityInfoDiv.innerHTML = "";

    // Kiểm tra nếu số người và ngày đi ngày về đã được nhập
    if (numberOfPeople && departureDate && returnDate) {
        // Hiển thị danh sách tour tương ứng với thành phố được chọn
        switch (selectedCity) {
            case "hanoi":
                displayTourList("Hà Nội");
                break;
            case "danang":
                displayTourList("Đà Nẵng");
                break;
            case "hochiminh":
                displayTourList("Hồ Chí Minh");
                break;
            // Thêm các trường hợp khác nếu cần
            default:
                cityInfoDiv.innerHTML = "<p>Chọn một thành phố để hiển thị thông tin.</p>";
        }
    } else {
        // Hiển thị thông báo nếu số người hoặc ngày đi/ngày về chưa được nhập
        cityInfoDiv.innerHTML = "<p>Vui lòng nhập đầy đủ thông tin số người và ngày đi/ngày về.</p>";
    }

    // Ngăn chặn form submit mặc định
    return false;
}

function displayTourList(cityName) {
    var cityInfoDiv = document.getElementById("cityInfo");

    // Hiển thị danh sách tour tương ứng với thành phố
    var tourListHTML = `<h3>Danh sách tour du lịch tại ${cityName}</h3>
        <ul>
            <li><a href="#" onclick="displayTourDetail('Tour 1')">Tour 1</a></li>
            <li><a href="#" onclick="displayTourDetail('Tour 2')">Tour 2</a></li>
            <li><a href="#" onclick="displayTourDetail('Tour 3')">Tour 3</a></li>
            <!-- Thêm các tour khác nếu cần -->
        </ul>`;
    cityInfoDiv.innerHTML = tourListHTML;
}

function displayTourDetail(tourName) {
    // Mở modal hoặc thực hiện các hành động khác để hiển thị chi tiết tour
    alert("Thông tin chi tiết về " + tourName);
}
