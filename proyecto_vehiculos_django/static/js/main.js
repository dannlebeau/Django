const brandsList = document.querySelector(".brands-list");

function cloneBrands() {
  const brands = brandsList.querySelectorAll(".brand-item");
  brands.forEach((brand) => {
    const clonedBrand = brand.cloneNode(true);
    brandsList.appendChild(clonedBrand);
  });
}

cloneBrands();
