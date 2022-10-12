function storageAvailable(type) {
    let storage;
    try {
        storage = window[type];
        const x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch (e) {
        return e instanceof DOMException && (
            // everything except Firefox
            e.code === 22 ||
            // Firefox
            e.code === 1014 ||
            // test name field too, because code might not be present
            // everything except Firefox
            e.name === 'QuotaExceededError' ||
            // Firefox
            e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
            // acknowledge QuotaExceededError only if there's something already stored
            (storage && storage.length !== 0);
    }
}

$(function() {
    if (storageAvailable('localStorage')) {
        $hw = $(".hw");
        $hw.addClass("hwtick-0");
        $hw.each(function() {
            $this = $(this);
            $hwid = $this.attr("data-hwid");
            ls_hwstat = localStorage.getItem("hwstat-" + $hwid);
            if (ls_hwstat == "1") {
                $this.removeClass("hwtick-0");
                $this.addClass("hwtick-1");
            }
        });
        $hw.click(function(e) {
            e.preventDefault();
            $this = $(this);
            $hwid = $this.attr("data-hwid");
            if ($this.hasClass("hwtick-1")) {
                localStorage.setItem("hwstat-" + $hwid,"0");
                $this.removeClass("hwtick-1");
                $this.addClass("hwtick-0");
            } else {
                localStorage.setItem("hwstat-" + $hwid,"1");
                $this.removeClass("hwtick-0");
                $this.addClass("hwtick-1");
            }
        });
    }
    else {
        $("#noLocalStorage").show();
    }

})
