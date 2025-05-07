$(document).ready(function () {
    const $sliderWrapper = $('.slider-wrapper');
    const $prevButton = $('.slider-prev');
    const $nextButton = $('.slider-next');
    const $cards = $('.slider-card');

    let currentIndex = 0;
    console.log($($cards[0]).width(), $($cards[0]).outerWidth(true));
    const totalCards = $cards.length;

    const cardWidth = $cards.outerWidth(true);
    let position = -cardWidth;
    const $firstClone = $cards.first().clone();
    const $lastClone = $cards.last().clone();

    $sliderWrapper.append($firstClone);
    $sliderWrapper.prepend($lastClone);
    const adjustedTotal = totalCards + 2;
    $sliderWrapper.css('transform', `translateX(${position}px)`);

    function moveSlider(direction) {
        if (direction === 'next') {
            console.log('here');
            console.log(currentIndex, totalCards);
            if (currentIndex >= totalCards) {
                // Reset to first card instantly, then move to next
                currentIndex = 0;
                position = -cardWidth; // Set position to first card
                console.log("position", position);
                $sliderWrapper.css({ transition: 'none', transform: `translateX(${position}px)` });

                // After reset, apply the transition for smooth sliding
                setTimeout(() => {
                    currentIndex++;
                    position -= cardWidth;
                    console.log("position", position);
                    $sliderWrapper.css({ transition: 'transform 0.5s ease-in-out', transform: `translateX(${position}px)` });
                }, 50);
            } else {
                currentIndex++;
                console.log("position1", position);
                position -= cardWidth;
                console.log("position", position);
                $sliderWrapper.css({ transition: 'transform 0.5s ease-in-out', transform: `translateX(${position}px)` });
            }
        } else if (direction === 'prev') {
            if (currentIndex <= 0) {
                currentIndex = totalCards - 1;
                position = -totalCards * cardWidth;
                console.log("position", position);
                $sliderWrapper.css({ transition: 'none', transform: `translateX(${position}px)` });

                setTimeout(() => {
                    currentIndex--;
                    position += cardWidth;
                    console.log("position", position);
                    $sliderWrapper.css({ transition: 'transform 0.5s ease-in-out', transform: `translateX(${position}px)` });
                }, 50);
            } else {
                currentIndex--;
                position += cardWidth;
                console.log("position", position);
                $sliderWrapper.css({ transition: 'transform 0.5s ease-in-out', transform: `translateX(${position}px)` });
            }
        }
    }

    // Event listeners for buttons
    $nextButton.on('click', function () {
        moveSlider('next');
    });

    $prevButton.on('click', function () {
        moveSlider('prev');
    });
    // $(document).ready(function () {
    //     // Dummy data for the cards
    //     const dummyData = [
    //         { image: 'images/artist1.jpeg', title: 'John Doe', description: 'Famous artist from UK.' },
    //         { image: 'images/artist2.jpeg', title: 'Jane Smith', description: 'Renowned artist from Canada.' },
    //         { image: 'images/artist3.jpeg', title: 'Samuel Lee', description: 'Top artist with a global fanbase.' },
    //         { image: 'images/artist4.jpeg', title: 'Emma Clark', description: 'Singer-songwriter from Australia.' },
    //         { image: 'images/artist5.jpeg', title: 'Chris Johnson', description: 'Music producer and DJ.' },
    //         { image: 'images/artist6.jpeg', title: 'Maria Brown', description: 'International music sensation.' },
    //         { image: 'images/artist7.jpeg', title: 'David King', description: 'Chart-topping singer from New York.' },
    //         { image: 'images/artist8.jpeg', title: 'Sophia White', description: 'Up-and-coming pop artist.' },
    //         { image: 'images/artist9.jpeg', title: 'Lucas Green', description: 'Rock artist with unique style.' },
    //         { image: 'images/artist10.jpeg', title: 'Olivia Gray', description: 'Multi-talented artist and songwriter.' }
    //     ];

    //     // Loop through each card and replace the content dynamically
    //     $('.slider-card').each(function (index) {
    //         if (dummyData[index]) {
    //             const data = dummyData[index];

    //             // Set the image, title, and description dynamically
    //             $(this).find('.card-title').text(data.title);
    //             $(this).find('.card-text').text(data.description);
    //         }
    //     });
    // });

});
