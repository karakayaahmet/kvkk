var $profileImgDiv = document.getElementById("profile-img-div"),
    $profileImg = document.getElementById("profile-img"),
    $changePhoto = document.getElementById("change-photo"),
    $xPosition = document.getElementById("x-position"),
    $yPosition = document.getElementById("y-position"),
    $saveImg = document.getElementById("save-img"),
    $loader = document.getElementById("loader"),
    $cancelImg = document.getElementById("cancel-img"),
    $profileImgInput = document
      .getElementById("profile-img-input"),
    $profileImgConfirm = document
      .getElementById("profile-img-confirm"),
    $error = document.getElementById("error");

var currentProfileImg = "",
    profileImgDivW = getSizes($profileImgDiv).elW,
    NewImgNatWidth = 0,
    NewImgNatHeight = 0,
    NewImgNatRatio = 0,
    NewImgWidth = 0,
    NewImgHeight = 0,
    NewImgRatio = 0,
    xCut = 0,
    yCut = 0;

makeSquared($profileImgDiv);

$changePhoto.addEventListener("change", function() {
  currentProfileImg = $profileImg.src;
  showPreview(this, $profileImg);
  $loader.style.width = "100%";
  $profileImgInput.style.display = "none";
  $profileImgConfirm.style.display = "flex";
  $error.style.display = "none";
});

$xPosition.addEventListener("input", function() {
  $profileImg.style.left = -this.value + "px";
  xCut = this.value;
  yCut = 0;
});

$yPosition.addEventListener("input", function() {
  $profileImg.style.top = -this.value + "px";
  yCut = this.value;
  xCut = 0;
});

$saveImg.addEventListener("click", function() {
  cropImg($profileImg);
  resetAll(true);
});

$cancelImg.addEventListener("click", function() {
  resetAll(false);
});

window.addEventListener("resize", function() {
  makeSquared($profileImgDiv);
  profileImgDivW = getSizes($profileImgDiv).elW;
});

function makeSquared(el) {
  var elW = el.clientWidth;
  el.style.height = elW + "px";
}

function showPreview(input, el) {
  var reader = new FileReader();
  reader.readAsDataURL(input.files[0]);
  if (input.files && input.files[0]) {
    reader.onload = function(e) {
      setTimeout(function() {
        el.src = e.target.result;
      }, 300);

      var poll = setInterval(function() {
        if (el.naturalWidth && el.src != currentProfileImg) {
          clearInterval(poll);
          setNewImgSizes(el);
          setTimeout(function() {
            $loader.style.width = "0%";
            $profileImg.style.opacity = "1";
          }, 1000);
        }
      }, 100);
    };
  } else {
    return;
  }
}

function setNewImgSizes(el) {
  if (getNatSizes(el).elR > 1) {
    el.style.width = "auto";
    el.style.height = "100%";
    newImgWidth = getSizes(el).elW;
    $xPosition.style.display = "block";
    $yPosition.style.display = "none";
    $xPosition.max = newImgWidth - profileImgDivW;
  } else if (getNatSizes(el).elR < 1) {
    el.style.width = "100%";
    el.style.height = "auto";
    newImgHeight = getSizes(el).elH;
    $xPosition.style.display = "none";
    $yPosition.style.display = "block";
    $yPosition.max = newImgHeight - profileImgDivW;
  } else if (getNatSizes(el).elR == 1) {
    el.style.width = "100%";
    el.style.height = "100%";
    $xPosition.style.display = "none";
    $yPosition.style.display = "none";
  }
}

function getNatSizes(el) {
  var elW = el.naturalWidth,
    elH = el.naturalHeight,
    elR = elW / elH;
  return {
    elW: elW,
    elH: elH,
    elR: elR
  };
}

function getSizes(el) {
  var elW = el.clientWidth,
    elH = el.clientHeight,
    elR = elW / elH;
  return {
    elW: elW,
    elH: elH,
    elR: elR
  };
}

function cropImg(el) {
  var natClientImgRatio = getNatSizes(el).elW / getSizes(el).elW;
  (myCanvas = document.getElementById("croppedPhoto")),
    (ctx = myCanvas.getContext("2d"));
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, 400, 400);
  ctx.drawImage(
    el,
    xCut * natClientImgRatio,
    yCut * natClientImgRatio,
    profileImgDivW * natClientImgRatio,
    profileImgDivW * natClientImgRatio,
    0,
    0,
    400,
    400
  );
  var newProfileImgUrl = myCanvas.toDataURL("image/jpeg");
  $profileImg.src = newProfileImgUrl;
}

function resetAll(confirm) {
  if (!confirm) {
    $profileImg.src = currentProfileImg;
  }
  $changePhoto.value = "";
  $profileImgInput.style.display = "block";
  $profileImgConfirm.style.display = "none";
  $profileImg.style.left = "0";
  $profileImg.style.top = "0";
  $profileImg.style.width = "100%";
  $profileImg.style.height = "100%";
  $xPosition.style.display = "none";
  $yPosition.style.display = "none";
  $xPosition.value = "0";
  $yPosition.value = "0";
  xCut = "0";
  yCut = "0";
}

function checkMinSizes(el) {
  if (getNatSizes(el).elW > 400 && getNatSizes(el).elH > 400) {
    return true;
  } else {
    return false;
  }
}
