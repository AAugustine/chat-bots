/* eslint-disable no-undef */
/**
* Responds to a MESSAGE event in Hangouts Chat.
*
* @param {Object} event the event object from Hangouts Chat
*/
// eslint-disable-next-line no-unused-vars
function onMessage(event) {
  var url = 'https://dog.ceo/api/breeds/image/random';
  var dogPic = JSON.parse(UrlFetchApp.fetch(url).getContentText());
  
  var image = dogPic;
  Logger.log(image.message);
  
  return {
   "cards": [
    {
      "sections": [
        {
          "widgets": [
            {
              "image": {
                "imageUrl": image.message
                }
              }
           
          ]
        }
      ]
    }
  ] 
  }
}

/**
* Responds to an ADDED_TO_SPACE event in Hangouts Chat.
*
* @param {Object} event the event object from Hangouts Chat
*/
// eslint-disable-next-line no-unused-vars
function onAddToSpace(event) {
  var message = 'Woof, thank you for adding me, ' + event.user.displayName + '!';
  return { 'text': message };
}

/**
* Responds to a REMOVED_FROM_SPACE event in Hangouts Chat.
*
* @param {Object} event the event object from Hangouts Chat
*/
// eslint-disable-next-line no-unused-vars
function onRemoveFromSpace(event) {
  // eslint-disable-next-line no-console
  console.info('Bot removed from ', event.space.name);
}