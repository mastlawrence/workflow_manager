import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Card, CardBody, CardHeader, Container, Flex, Heading, Image, Link, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Container>
  <Flex>
  <Box>
  <Image src={`/thesis_logo.PNG`}/>
</Box>
</Flex>
  <VStack justifyContent={`space_between`}>
  <Card sx={{"fontFamily": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"backgroundColor": "PaleGreen", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading size={`lg`} sx={{"fontFamily": "Tahoma", "fontWeight": "500"}}>
  <Link as={NextLink} href={`/extractables`}>
  {`Extractables`}
</Link>
  <Image src={`bottle1.PNG`} sx={{"margin-left": "30px", "width": "60px", "display": "inline-block"}}/>
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`
    Manage MassHunter data of extractables compounds from primary packaging
    systems. Review and update extractables RRT databases for non-volatile,
    semi-volatile, and non-volatile compounds. Review literature regarding
    analysis of extractables compounds in primary packaging systems.
    `}
</Text>
</CardBody>
</Card>
  <Card sx={{"fontFamily": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"backgroundColor": "LightBlue", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading size={`lg`} sx={{"fontFamily": "Tahoma", "fontWeight": "500"}}>
  <Link as={NextLink} href={`/leachables`}>
  {`Leachables`}
</Link>
  <Image src={`/chem_illustration.PNG`} sx={{"margin-left": "40px", "width": "70px", "display": "inline-block"}}/>
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`
    Manage MassHunter data of leachables compounds from device and drug 
    product studies. Review previous leachables profiles and validation
    studies. Review ICH and FDA expectations of leachables validation
    acceptance criteria.
    `}
</Text>
</CardBody>
</Card>
  <Card sx={{"fontFamily": "Tahoma", "width": "800px", "border": "2px solid", "_hover": {"backgroundColor": "LightGrey", "transition": "0.3s"}}}>
  <CardHeader>
  <Heading size={`lg`} sx={{"fontFamily": "Tahoma", "fontWeight": "500"}}>
  <Link as={NextLink} href={`/literature`}>
  {`Literature`}
</Link>
  <Image src={`/book_icon.PNG`} sx={{"margin-left": "55px", "width": "70px", "display": "inline-block"}}/>
</Heading>
</CardHeader>
  <CardBody>
  <Text>
  {`
    Review extractables and leachables literature from outside studies. 
    Search for references to compounds identified in extractables studies.
    Read about previous work performed on similar primary packaging systems.
    `}
</Text>
</CardBody>
</Card>
</VStack>
</Container>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
