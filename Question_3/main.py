import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


if __name__ == "__main__":
    data = pd.read_csv('user_data.csv')

    PMF_column_titles = ['P(B)', 'P(T)', 'P(S)', 'P(A)']

    # P(B)
    B_PMF = data['Bought'].value_counts(normalize=True).sort_index()

    # P(T)
    T_PMF = data['Spender Type'].value_counts(normalize=True).sort_index()

    # P(S)
    S_PMF = data['Sex'].value_counts(normalize=True).sort_index()

    # P(A)
    A_PMF = data['Age'].sort_index().value_counts(normalize=True).sort_index()

    PMFS = [B_PMF, T_PMF, S_PMF, A_PMF]

    # Plotting the PMFS
    for i, PMF in enumerate(PMFS):

        plt.figure()
        PMF.sort_index().plot(kind='bar')
        plt.title(PMF_column_titles[i])
        if i == 3:
            ax = plt.gca()
            ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
        plt.show()

    Conditional_PMF_column_titles = ['P(T|B=0)', 'P(S|B=0)', 'P(A|B=0)', 'P(T|B=1)', 'P(S|B=1)', 'P(A|B=1)']

    # P(T|B=0)
    T_Given_B_Equals_0_PMF = data[data['Bought'] == 0]['Spender Type'].value_counts(normalize=True).sort_index()

    # P(S|B=0)
    S_Given_B_Equals_0_PMF = data[data['Bought'] == 0]['Sex'].value_counts(normalize=True).sort_index()

    # P(A|B=0)
    A_Given_B_Equals_0_PMF = data[data['Bought'] == 0]['Age'].value_counts(normalize=True).sort_index()

    # P(T|B=1)
    T_Given_B_Equals_1_PMF = data[data['Bought'] == 1]['Spender Type'].value_counts(normalize=True).sort_index()

    # P(S|B=1)
    S_Given_B_Equals_1_PMF = data[data['Bought'] == 1]['Sex'].value_counts(normalize=True).sort_index()

    # P(A|B=1)
    A_Given_B_Equals_1_PMF = data[data['Bought'] == 1]['Age'].value_counts(normalize=True).sort_index()

    Conditional_PMFS_Given_B_Equals_0 = [T_Given_B_Equals_0_PMF, S_Given_B_Equals_0_PMF, A_Given_B_Equals_0_PMF]
    Conditional_PMFS_Given_B_Equals_1 = [T_Given_B_Equals_1_PMF, S_Given_B_Equals_1_PMF, A_Given_B_Equals_1_PMF]

    # Plotting the Conditional PMFS
    for i, PMF in enumerate(Conditional_PMFS_Given_B_Equals_0):
        plt.figure()
        PMF.plot(kind='bar')
        plt.title(Conditional_PMF_column_titles[i])
        if i == 2:
            ax = plt.gca()
            ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
        plt.show()

    for i, PMF in enumerate(Conditional_PMFS_Given_B_Equals_1):
        plt.figure()
        PMF.plot(kind='bar')
        plt.title(Conditional_PMF_column_titles[i+3])
        if i == 2:
            ax = plt.gca()
            ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
        plt.show()

    # P(T=1 | B=0)
    P_T1_Given_B0 = T_Given_B_Equals_0_PMF[1]

    # P(S=0 | B=0)
    P_S0_Given_B0 = S_Given_B_Equals_0_PMF[0]

    # P(A<=67 | B=0)
    P_ALTE67_Given_B0 = 0
    for age in A_Given_B_Equals_0_PMF.index:
        if age <= 67:
            P_ALTE67_Given_B0 += A_Given_B_Equals_0_PMF[age]

    # P(T=1, S=0, A<=67 | B=0) = P(T=1 | B=0) * P(S=0 | B=0) * P(A<=67 | B=0) * P(B=0)
    P_T1_S0_ALTE67_Given_B0 = (P_T1_Given_B0 * P_S0_Given_B0 * P_ALTE67_Given_B0 * B_PMF[0])

    # P(T=1 | B=1)
    P_T1_Given_B1 = T_Given_B_Equals_1_PMF[1]

    # P(S=0 | B=1)
    P_S0_Given_B1 = S_Given_B_Equals_1_PMF[0]

    # P(A<=67 | B=1)
    P_ALTE67_Given_B1 = 0
    for age in A_Given_B_Equals_1_PMF.index:
        if age <= 67:
            P_ALTE67_Given_B1 += A_Given_B_Equals_1_PMF[age]

    # P(T=1, S=0, A<=67 | B=1) = P(T=1 | B=1) * P(S=0 | B=1) * P(A<=67 | B=1) * P(B=1)
    P_T1_S0_ALTE67_Given_B1 = (P_T1_Given_B1 * P_S0_Given_B1 * P_ALTE67_Given_B1 * B_PMF[1])

    # P(T=1, S=0, A<=67) = P(T=1, S=0, A<=67 | B=0) * P(B=0) + P(T=1, S=0, A<=67 | B=1) * P(B=1)
    P_T1_S0_ALTE67 = (P_T1_S0_ALTE67_Given_B0 * B_PMF[0]) + (P_T1_S0_ALTE67_Given_B1 * B_PMF[1])

    # P(B=0 | T=1, S=0, A<=67) = P(T=1, S=0, A<=67 | B=0) * P(B=0) / P(T=1, S=0, A<=67)
    P_B0_given_T1_S0_ALTE67 = (P_T1_S0_ALTE67_Given_B0 * B_PMF[0]) / P_T1_S0_ALTE67

    # P(B=1 | T=1, S=0, A<=67) = P(T=1, S=0, A<=67 | B=1) * P(B=1) / P(T=1, S=0, A<=67)
    P_B1_given_T1_S0_ALTE67 = (P_T1_S0_ALTE67_Given_B1 * B_PMF[1]) / P_T1_S0_ALTE67

    print("P(B=0 | T=1, S=0, A<=67) = ", P_B0_given_T1_S0_ALTE67)
    print("P(B=1 | T=1, S=0, A<=67) = ", P_B1_given_T1_S0_ALTE67)

    # Prediction
    if P_B1_given_T1_S0_ALTE67 > P_B0_given_T1_S0_ALTE67:
        print("\nThe user will buy the product.")
    else:
        print("\nThe user will not buy the product.")