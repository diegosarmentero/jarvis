import QtQuick 1.1

Rectangle {

    id: frame
    width: 400
    height: 80
    color: "black"
    opacity: 0.5
    radius: 15
    border.color: "#aae3ef"
    border.width: 2

    Text{
        id: text
        text: "Esta es una notification del sistema."
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

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
    }

    states: State {
         name: "entered"; when: mouseArea.containsMouse
         PropertyChanges { target: frame; opacity: 1 }
     }

    transitions: Transition {
        reversible: true
        NumberAnimation { properties: "opacity"; from: 0.5; to: 1; duration: 500 }
    }

}
