import streamlit as st
import Adding_matrices as am
import multiplying_matrices as mm
import transpose_matrices as tm
import inverse_matices as im
import determinant_matrices as dm

option = st.sidebar.radio(
    'Choose Method:',
    ('Home','Addition of Matrices', 'Multiplication of Matrices', 'Transpose of Matrices', 'Inverse of Matrices',
     'Determinant of Matrices'))

if option == 'Home':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #96C3EB ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Matrix Calculator')
    st.divider()
    st.markdown("The term **matrix** has several meanings depending on the context.")
    st.markdown("If you’re dealing with matrices, the **Matrix Calculator** is a" 
            "powerful tool that allows you to perform various operations on matrices.")

    st.write("-------")
elif option == 'Addition of Matrices':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #6ACCBC ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Addition of Matrix')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Bahnschrift'; text-align: wide">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                    Matrix A
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                        Matrix B
                        </h1>
                    """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)
    print(st.session_state)
    calculate = st.button("Calculate", key='add_button')
    if calculate:
        import time
        import streamlit as st

        with st.spinner('Calculating'):
            time.sleep(2)
            st.header("Sum of Matrix A and B")
        try:
            matrix_Result = am.get_sumOfMatrices(matA, matB)
            col1, col2,col3 = st.columns(3)

            with col2:
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
        except ValueError as e:
            st.error(str(e))
elif option == 'Multiplication of Matrices':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #D1B15B ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Multiplication of Matrix')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Bahnschrift'; text-align: wide">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                    Matrix A
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                        Matrix B
                        </h1>
                    """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)
    print(st.session_state)
    calculate = st.button("Calculate", key='add_button')
    if calculate:
        import time
        import streamlit as st

        with st.spinner('Calculating'):
            time.sleep(2)
        st.header("Product of Matrix A and B")
        try:
            matrix_Result = mm.multiplying_matrices(matA, matB)
            col6, col7, col8 = st.columns(3)
            with col7:
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
        except ValueError as e:
            st.error(str(e))
elif option == 'Transpose of Matrices':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #14AAF5 ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Transpose of Matrix')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Bahnschrift'; text-align: wide">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                    Matrix A
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                        Matrix B
                        </h1>
                    """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)
    print(st.session_state)
    calculate = st.button("Calculate", key='add_button')
    if calculate:
        import time
        import streamlit as st

        with st.spinner('Calculating'):
            time.sleep(2)
        st.subheader("Transpose of Matrix A and B")
        try:
            matrix_Result = tm.transpose_matrices(matA, matB)
            col8, = st.columns(1)
            with col8:
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
        except IndexError as e:
            st.error(str(e))
elif option == 'Inverse of Matrices':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #EB96EB ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Inverse of Matrix')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Bahnschrift'; text-align: wide">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                    Matrix A
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                        Matrix B
                        </h1>
                    """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)
    print(st.session_state)
    calculate = st.button("Calculate", key='add_button')
    if calculate:
        import time
        import streamlit as st

        with st.spinner('Calculating'):
            time.sleep(2)
        inv_matA, inv_matB = im.inverse_matrices(matA, matB)
        if inv_matA is not None and inv_matB is not None:
            col6, col7 = st.columns(2)
            with col6:
                st.subheader("Inverse of Matrix A")
                for row_index in range(len(inv_matA)):
                    for col_index in range(len(inv_matA[row_index])):
                        st.text_input("", value=str(inv_matA[row_index][col_index]),
                                      key=f'A_{row_index + 1}Acol{col_index + 1}')
            with col7:
                st.subheader("Inverse of Matrix B")
                for row_index in range(len(inv_matB)):
                    for col_index in range(len(inv_matB[row_index])):
                        st.text_input("", value=str(inv_matB[row_index][col_index]),
                                      key=f'B_{row_index + 1}Bcol{col_index + 1}')
elif option == 'Determinant of Matrices':
    st.markdown(
        """
        <style>
        .stApp{
            background-color : #FF8D85 ;

        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Determinant of Matrix')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Bahnschrift'; text-align: wide">
                Enter the size of the matrices:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    with col3:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
                    <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                    Matrix A
                    </h1>
                """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

    with col5:
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Bahnschrift';">
                        Matrix B
                        </h1>
                    """, unsafe_allow_html=True)
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
    matA = []
    matB = []
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Arow{i + 1}Acol{j + 1}":
                    rowSum.append(st.session_state[value])
        matA.append(rowSum)
    print(matA)
    for i in range(row):
        rowSum = []
        for j in range(column):
            for value in st.session_state:
                if value == f"Brow{i + 1}Bcol{j + 1}":
                    rowSum.append(st.session_state[value])
        matB.append(rowSum)
    print(matB)
    print(st.session_state)
    calculate = st.button("Calculate", key='add_button')
    if calculate:
        import time
        import streamlit as st

        with st.spinner('Calculating'):
            time.sleep(2)
        try:
            det_matA, det_matB = dm.determinant_matrices(matA, matB)
            col4, col5 = st.columns(2)
            with col4:
                st.subheader("Determinant of Matrix A")
                st.text_input("", value=str(det_matA))
            with col5:
                st.subheader("Determinant of Matrix B")
                st.text_input("", value=str(det_matB))
        except ValueError as e:
            st.error(str(e))
