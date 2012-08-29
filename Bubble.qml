import QtQuick 1.1

Rectangle {

    id: frame
    width: 400
    height: 80
    color: "black"
    opacity: 0.6
    radius: 15
    border.color: "#aae3ef"
    border.width: 2

    Text{
        id: text
        text: "This is a Notification"
        wrapMode: Text.WordWrap
        font.pixelSize: 18
        font.bold: true
        anchors.fill: parent
        anchors.topMargin: 20
        anchors.leftMargin: 20
        anchors.rightMargin: 20
        anchors.bottomMargin: 20
        color: "white"
    }

    Component.onCompleted: {
        height = text.paintedHeight + 40
    }


}
